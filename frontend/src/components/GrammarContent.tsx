import React from 'react';

interface GrammarContentProps {
  content: string;
}

/**
 * Parses and renders grammar content with smart table detection.
 * Detects patterns like verb conjugations, pronoun tables, and structured lists.
 */
export function GrammarContent({ content }: GrammarContentProps) {
  if (!content) return null;

  // Split content into paragraphs/sections
  const sections = content.split(/\n\n+/);

  return (
    <div className="space-y-4">
      {sections.map((section, idx) => (
        <GrammarSection key={idx} content={section.trim()} />
      ))}
    </div>
  );
}

function GrammarSection({ content }: { content: string }) {
  // Check if this section looks like a conjugation table
  const conjugationPattern = /\b(je|tu|il|elle|nous|vous|ils|elles)\b.*[-=:→]/i;
  const pronounPattern = /\b(moi|toi|lui|elle|nous|vous|eux|elles)\b.*[-=:→]/i;
  const articlePattern = /\b(le|la|les|un|une|des)\b.*[-=:→]/i;

  // Check for table-like patterns (lines with consistent delimiters)
  const lines = content.split('\n').filter(line => line.trim());
  const hasTableStructure = lines.length >= 2 && lines.every(line =>
    line.includes(' - ') || line.includes(': ') || line.includes(' → ') || line.includes(' = ')
  );

  // Check for conjugation-specific patterns
  const isConjugationTable = lines.some(line => conjugationPattern.test(line));
  const isPronounTable = lines.some(line => pronounPattern.test(line)) && lines.length >= 3;
  const isArticleTable = lines.some(line => articlePattern.test(line)) && lines.length >= 2;

  if (hasTableStructure && (isConjugationTable || isPronounTable || isArticleTable)) {
    return <StructuredTable lines={lines} />;
  }

  // Check for simple list pattern (lines starting with - or *)
  const isSimpleList = lines.length >= 2 && lines.every(line =>
    line.trim().startsWith('-') || line.trim().startsWith('*') || line.trim().startsWith('•')
  );

  if (isSimpleList) {
    return (
      <ul className="space-y-1 text-gray-700">
        {lines.map((line, idx) => (
          <li key={idx} className="flex items-start gap-2">
            <span className="text-primary-500">•</span>
            <span>{line.replace(/^[-*•]\s*/, '')}</span>
          </li>
        ))}
      </ul>
    );
  }

  // Check for numbered list
  const isNumberedList = lines.length >= 2 && lines.every(line =>
    /^\d+[.)]\s/.test(line.trim())
  );

  if (isNumberedList) {
    return (
      <ol className="space-y-1 text-gray-700 list-decimal list-inside">
        {lines.map((line, idx) => (
          <li key={idx}>{line.replace(/^\d+[.)]\s*/, '')}</li>
        ))}
      </ol>
    );
  }

  // Default: render as paragraph with preserved whitespace
  return (
    <p className="text-gray-700 whitespace-pre-wrap">{content}</p>
  );
}

function StructuredTable({ lines }: { lines: string[] }) {
  // Parse lines into key-value pairs
  const rows = lines.map(line => {
    // Try different delimiters
    const delimiters = [' → ', ' = ', ' - ', ': '];
    for (const delimiter of delimiters) {
      const idx = line.indexOf(delimiter);
      if (idx > 0) {
        return {
          left: line.substring(0, idx).trim(),
          right: line.substring(idx + delimiter.length).trim(),
        };
      }
    }
    return { left: line, right: '' };
  });

  // Detect if this is a conjugation table (pronouns in first column)
  const pronouns = ['je', 'tu', 'il', 'elle', "il/elle", "on", 'nous', 'vous', 'ils', 'elles', "ils/elles"];
  const isConjugation = rows.some(row =>
    pronouns.some(p => row.left.toLowerCase().startsWith(p))
  );

  // Detect if this is a tonic pronoun or similar table
  const tonicPronouns = ['moi', 'toi', 'lui', 'elle', 'nous', 'vous', 'eux', 'elles', 'soi'];
  const isTonicTable = rows.some(row =>
    tonicPronouns.some(p => row.left.toLowerCase() === p || row.right.toLowerCase().includes(p))
  );

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm border-collapse">
        <thead>
          <tr className="bg-primary-50 border-b border-primary-200">
            <th className="text-left py-2 px-3 font-semibold text-primary-800">
              {isConjugation ? 'Subject' : isTonicTable ? 'Pronoun' : 'French'}
            </th>
            <th className="text-left py-2 px-3 font-semibold text-primary-800">
              {isConjugation ? 'Conjugation' : isTonicTable ? 'Meaning/Use' : 'Meaning'}
            </th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row, idx) => (
            <tr
              key={idx}
              className={`border-b border-gray-100 ${idx % 2 === 0 ? 'bg-gray-50' : 'bg-white'}`}
            >
              <td className="py-2 px-3 font-medium text-gray-900">{row.left}</td>
              <td className="py-2 px-3 text-gray-700">{row.right}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GrammarContent;
