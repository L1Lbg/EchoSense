<h1>EchoSense</h1>

<p>
  EchoSense is a school project developed by <a href='https://lucabae.pages.dev' target='_blank'>Luca Baeyens</a> and <a href='https://madriddaniel.com/' target='_blank'>Daniel Madrid</a>.
  It is a virtual assistant that leverages AI to recognize speech and camera movements, allowing you to control your PC in a variety of ways:
</p>
<ul>
  <li>Manage files</li>
  <li>Search for information</li>
  <li>Open and interact with apps</li>
</ul>
<h2>Hardware</h2>
<p>
  <ul>
    <li>
      Raspberry Pi 5 + Kit
    </li>
  </ul>
</p>

<h2>Timeline</h2>
<ul>
  <li>
    <strong>
      13/12/24:
    </strong>
    Git repository creation. Scripts are made and almost ready to use.
    <br>
    Todo: Set up Raspberry Pi.
  </li>
  <li>
    <strong>
      20/12/24:
    </strong>
    Script now listens for wake word, and is directly connected to text processing.
    <br>
    Todo: Set up Raspberry Pi (arrives 1st of January).
    Train personalized wake word model.
    After text is processed, realise action.
  </li>
  <li>
    <strong>
      10/01/25:
    </strong>
    Raspberry Pi arrived (later than expected).
    Downloaded all O-LLama models and this GitHub repository.
    <br>
    Todo: Study the best AI model for performance on this Hardware, and continue developing the program.
  </li>
    <li>
    <strong>
      17/01/25:
    </strong>
    Added text to speech which will talk.
    Did some prompt engineering to improve outcome.
    Added actions processing so the script actually executes what's asked.
    <br>
    Todo: Study the best AI model for performance on this Hardware, and continue developing the program.
    <br/>
    Todo: Fix a bug where listener listens the first one but does not execute the rest of the script. Everything works after the seconds listening.
  </li>
</ul>
