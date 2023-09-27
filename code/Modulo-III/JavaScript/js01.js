

let years = new Map();
years.set(2000, "Año 2000");
years.set(2001, "Año 2001");
years.set(2002, "Año 2002");
years.set(2000, "Año xxxx");

console.log(years.get(2000));

console.log("--------------------------------------------");
for (const [key, value] of years.entries()) {
    console.log(key, value);
}