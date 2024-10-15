/** @type {import('tailwindcss').Config} */

const arbitraryWidthSafeList = () => {
  let ret = [];
  for (let i = 0; i < 101; i++) {
    ret.push(`w-[${i}%]`);
  }
  return ret;
};

module.exports = {
  content: ["./templates/**/*.html"],
  safelist: arbitraryWidthSafeList(),
  plugins: [require("flowbite/plugin")],
};
