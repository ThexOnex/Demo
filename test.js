// Function to format a date as YYYY-MM-DD
function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are zero-based
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Get the current date
const currentDate = new Date();
console.log("Current Date:", formatDate(currentDate));

// Get yesterday's date
const yesterday = new Date();
yesterday.setDate(currentDate.getDate() - 1);
console.log("Yesterday's Date:", formatDate(yesterday));
