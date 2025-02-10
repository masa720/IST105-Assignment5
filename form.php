<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h2>Welcome to the Interactive Treasure Hunt!</h2>
    <p>Enter your details to solve the puzzle and find the treasure.</p>
    <form action="process.php" method="post">
        <label for="number">Number(e.g., birth year):</label>
        <input type="number" name="number" required><br>

        <label for="text">Text(e.g., name or secret word):</label>
        <input type="text" name="text" require><br>

        <input type="submit" value="Solve the Puzzle">
    </form>
</body>
</html>
