import React from 'react';

interface GrammarContentProps {
  content: string;
}

/**
 * Parse markdown-style formatting in text
 */
function parseInlineFormatting(text: string): React.ReactNode[] {
  const parts: React.ReactNode[] = [];
  let remaining = text;
  let key = 0;

  while (remaining.length > 0) {
    // Check for bold (**text**)
    const boldMatch = remaining.match(/\*\*(.+?)\*\*/);
    if (boldMatch && boldMatch.index !== undefined) {
      // Add text before the match
      if (boldMatch.index > 0) {
        parts.push(<span key={key++}>{remaining.slice(0, boldMatch.index)}</span>);
      }
      // Add bold text
      parts.push(<strong key={key++} className="font-semibold">{boldMatch[1]}</strong>);
      remaining = remaining.slice(boldMatch.index + boldMatch[0].length);
    } else {
      // No more matches, add remaining text
      parts.push(<span key={key++}>{remaining}</span>);
      break;
    }
  }

  return parts;
}

/**
 * Parses and renders grammar content with smart table detection.
 * Supports markdown tables, lists, and formatted text.
 */
export function GrammarContent({ content }: GrammarContentProps) {
  if (!content) return null;

  // Split content into blocks
  const blocks = parseContentBlocks(content);

  return (
    <div className="space-y-4">
      {blocks.map((block, idx) => (
        <ContentBlock key={idx} block={block} />
      ))}
    </div>
  );
}

type Block =
  | { type: 'markdown-table'; rows: string[][] }
  | { type: 'list'; items: string[]; ordered: boolean }
  | { type: 'paragraph'; text: string };

function parseContentBlocks(content: string): Block[] {
  const blocks: Block[] = [];
  const lines = content.split('\n');
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];
    const trimmedLine = line.trim();

    // Skip empty lines
    if (!trimmedLine) {
      i++;
      continue;
    }

    // Check for markdown table (lines starting with |)
    if (trimmedLine.startsWith('|')) {
      const tableLines: string[] = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        tableLines.push(lines[i].trim());
        i++;
      }
      const tableBlock = parseMarkdownTable(tableLines);
      if (tableBlock) {
        blocks.push(tableBlock);
      }
      continue;
    }

    // Check for bullet list
    if (trimmedLine.startsWith('- ') || trimmedLine.startsWith('* ') || trimmedLine.startsWith('• ')) {
      const listItems: string[] = [];
      while (i < lines.length) {
        const listLine = lines[i].trim();
        if (listLine.startsWith('- ') || listLine.startsWith('* ') || listLine.startsWith('• ')) {
          listItems.push(listLine.replace(/^[-*•]\s*/, ''));
          i++;
        } else if (listLine === '') {
          i++;
          break;
        } else {
          break;
        }
      }
      if (listItems.length > 0) {
        blocks.push({ type: 'list', items: listItems, ordered: false });
      }
      continue;
    }

    // Check for numbered list
    if (/^\d+[.)]\s/.test(trimmedLine)) {
      const listItems: string[] = [];
      while (i < lines.length) {
        const listLine = lines[i].trim();
        if (/^\d+[.)]\s/.test(listLine)) {
          listItems.push(listLine.replace(/^\d+[.)]\s*/, ''));
          i++;
        } else if (listLine === '') {
          i++;
          break;
        } else {
          break;
        }
      }
      if (listItems.length > 0) {
        blocks.push({ type: 'list', items: listItems, ordered: true });
      }
      continue;
    }

    // Regular paragraph - collect consecutive non-special lines
    const paragraphLines: string[] = [];
    while (i < lines.length) {
      const pLine = lines[i];
      const pTrimmed = pLine.trim();

      // Stop at empty line or special block start
      if (!pTrimmed || pTrimmed.startsWith('|') ||
          pTrimmed.startsWith('- ') || pTrimmed.startsWith('* ') ||
          pTrimmed.startsWith('• ') || /^\d+[.)]\s/.test(pTrimmed)) {
        break;
      }

      paragraphLines.push(pLine);
      i++;
    }

    if (paragraphLines.length > 0) {
      blocks.push({ type: 'paragraph', text: paragraphLines.join('\n') });
    }
  }

  return blocks;
}

function parseMarkdownTable(lines: string[]): Block | null {
  if (lines.length < 2) return null;

  const rows: string[][] = [];

  for (const line of lines) {
    // Skip separator rows (|---|---|)
    if (/^\|[-:\s|]+\|$/.test(line)) continue;

    // Parse cells
    const cells = line
      .split('|')
      .map(cell => cell.trim())
      .filter((cell, idx, arr) => {
        // Filter out empty first/last cells from leading/trailing |
        if (idx === 0 && cell === '') return false;
        if (idx === arr.length - 1 && cell === '') return false;
        return true;
      });

    if (cells.length > 0) {
      rows.push(cells);
    }
  }

  if (rows.length === 0) return null;
  return { type: 'markdown-table', rows };
}

function ContentBlock({ block }: { block: Block }) {
  if (block.type === 'markdown-table') {
    return <MarkdownTable rows={block.rows} />;
  }

  if (block.type === 'list') {
    if (block.ordered) {
      return (
        <ol className="space-y-1 text-gray-700 list-decimal list-inside ml-2">
          {block.items.map((item, idx) => (
            <li key={idx}>{parseInlineFormatting(item)}</li>
          ))}
        </ol>
      );
    }
    return (
      <ul className="space-y-1 text-gray-700 ml-2">
        {block.items.map((item, idx) => (
          <li key={idx} className="flex items-start gap-2">
            <span className="text-primary-500 mt-1">•</span>
            <span>{parseInlineFormatting(item)}</span>
          </li>
        ))}
      </ul>
    );
  }

  // Paragraph
  return (
    <p className="text-gray-700 whitespace-pre-wrap">
      {parseInlineFormatting(block.text)}
    </p>
  );
}

function MarkdownTable({ rows }: { rows: string[][] }) {
  if (rows.length === 0) return null;

  const hasHeader = rows.length > 1;
  const headerRow = hasHeader ? rows[0] : null;
  const bodyRows = hasHeader ? rows.slice(1) : rows;

  return (
    <div className="overflow-x-auto my-3">
      <table className="w-full text-sm border-collapse border border-gray-200 rounded-lg">
        {headerRow && (
          <thead>
            <tr className="bg-primary-50">
              {headerRow.map((cell, idx) => (
                <th
                  key={idx}
                  className="text-left py-2 px-3 font-semibold text-primary-800 border-b border-primary-200"
                >
                  {parseInlineFormatting(cell)}
                </th>
              ))}
            </tr>
          </thead>
        )}
        <tbody>
          {bodyRows.map((row, rowIdx) => (
            <tr
              key={rowIdx}
              className={`border-b border-gray-100 ${rowIdx % 2 === 0 ? 'bg-white' : 'bg-gray-50'}`}
            >
              {row.map((cell, cellIdx) => (
                <td
                  key={cellIdx}
                  className={`py-2 px-3 ${cellIdx === 0 ? 'font-medium text-gray-900' : 'text-gray-700'}`}
                >
                  {parseInlineFormatting(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GrammarContent;
