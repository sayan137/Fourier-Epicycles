<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fourier Epicycle Drawing</title>
</head>
<body>
    <h1>Fourier Epicycle Drawing</h1>
    <p>
        This project demonstrates the generation of Fourier epicycles to draw complex shapes from an SVG path. 
        The technique uses Fourier Transform to decompose a set of points extracted from an SVG file into 
        Fourier coefficients. These coefficients are then used to visualize the drawing process as a series 
        of rotating arrows (epicycles).
    </p>
    
   <h2>Features</h2>
    <ul>
        <li>Extracts path data from an SVG file.</li>
        <li>Performs Fourier Transform to compute coefficients.</li>
        <li>Visualizes the epicycles using Plotly, showing how the shape is drawn over time.</li>
        <li>Generates an interactive HTML output with animations.</li>
    </ul>

  <h2>How to Use</h2>
    <ol>
        <li>Ensure you have the following Python packages installed: 
            <code>numpy</code>, <code>plotly</code>, <code>matplotlib</code>, <code>svgpathtools</code>, and <code>scipy</code>.
        </li>
        <li>Place your desired SVG file in the project directory and update its path in the code.</li>
        <li>Run the Python script to generate the interactive HTML file.</li>
        <li>Open the generated HTML file in a web browser to view the animation.</li>
    </ol>

  <h2>Code Inspirations</h2>
    <p>
        This implementation is inspired by insightful video series on fft by Grant Sanderson aka 3b1b. And whole thing wouldnt be that flawless without lucid explanation of fourier epicycles by Burkard Polster(aka mathologer)'s lucid explanation of the topic.
    </p>

  <h2>Output</h2>
    <p>
        You can view the generated animation by opening the HTML file in a web browser

   </p>

</body>
</html>
