var TestSuit = require("nist-randomness-test-suite");

var BBS = ((x) => {
  p = 104701;
  q = 103651;
  m = p * q;
  return () => {
    x = (x * x) % m;
    return x % 2;
  };
})(101399);

let testSuite = new TestSuit(0.001);

let frequencyTest = testSuite.frequencyTest(BBS);
let runsTest = testSuite.runsTest(BBS);
let binaryMatrixRankTest = testSuite.binaryMatrixRankTest(BBS);
let nonOverlappingTemplateMatchingTest = testSuite.nonOverlappingTemplateMatchingTest(BBS);

console.log(frequencyTest, runsTest, binaryMatrixRankTest, nonOverlappingTemplateMatchingTest)