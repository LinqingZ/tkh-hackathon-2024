import React from 'react';

class TextDiff extends React.Component {
  highlightChanges(originalText, improvedText) {
    const originalWords = originalText.split(' ');
    const improvedWords = improvedText.split(' ');

    let highlightedText = '';

    for (let i = 0; i < originalWords.length; i++) {
      if (originalWords[i] !== improvedWords[i]) {
        highlightedText += `<span style="background-color: grey">${originalWords[i]}</span>`;
      } else {
        highlightedText += originalWords[i];
      }
      highlightedText += ' ';
    }

    return <div dangerouslySetInnerHTML={{ __html: highlightedText }} />;
  }

  render() {
    const originalFile = 'This is the original text file.';
    const improvedFile = 'This is the improved text file with some changes.';

    const highlightedContent = this.highlightChanges(originalFile, improvedFile);

    return (
      <div>
        <h2>Original File</h2>
        <pre>{originalFile}</pre>
        <h2>Improved File</h2>
        <pre>{improvedFile}</pre>
        <h2>Highlighted Changes</h2>
        <div>{highlightedContent}</div>
      </div>
    );
  }
}

export default TextDiff;