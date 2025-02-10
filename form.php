<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h2>Welcome to the Interactive Treasure Hunt!</h2>
    <form action="process.php" method="post">
        <label for="number">Number:</label>
        <input type="number" name="number" required placeholder="e.g., birth year"><br>

        <label for="text">Text:</label>
        <input type="text" name="text" require placeholder="e.g., name or secret word"><br>

        <input type="submit" value="Solve the Puzzle">
    </form>
</body>
</html>
