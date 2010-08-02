#using <mscorlib.dll>
#using <System.dll>

using namespace System;
using namespace System::Text::RegularExpressions;

__gc class MyClass {
public:
    static int i=0;

        static String* ReplaceCC(Match* m) {
                // Replace each Regex cc match with the number of the occurrence.
                        i++;
                                return i.ToString();
                                    }
                                    };

                                    int main() {
                                        String* sInput, * sRegex;

                                            // The string to search.
                                                sInput = S"aabbccddeeffcccgghhcccciijjcccckkcc";

                                                    // A very simple regular expression.
                                                        sRegex = S"cc";

                                                            Regex* r = new Regex(sRegex);

                                                                // Assign the replace method to the MatchEvaluator delegate.
                                                                    MatchEvaluator* myEvaluator = new MatchEvaluator(0, &MyClass::ReplaceCC);

                                                                        // Write out the original string.
                                                                            Console::WriteLine(sInput);

                                                                                // Replace matched characters using the delegate method.
                                                                                    sInput = r->Replace(sInput, myEvaluator);

                                                                                        // Write out the modified string.
                                                                                            Console::WriteLine(sInput);
                                                                                            }

