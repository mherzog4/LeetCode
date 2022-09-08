/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
 let prefix = ''
 if (strs.length === 0) return prefix
 for (let i = 0; i < strs[0].length; i++) {
     const char = strs[0][i]
     for (let j = 0; j < strs.length; j++) {
         if (strs[j][i] !== char) return prefix
     }
     prefix = prefix + char
 }
    return prefix
};