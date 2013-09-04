# -*- coding: utf-8 -*-
from diff_cover.tests.helpers import line_numbers, git_diff_output, unittest
    def test_git_unicode_filename(self):

        # Filenames with unicode characters have double quotes surrounding them
        # in the git diff output.
        diff_str = dedent("""
            diff --git "a/unic\303\270\342\210\202e\314\201.txt" "b/unic\303\270\342\210\202e\314\201.txt"
            new file mode 100644
            index 0000000..248ebea
            --- /dev/null
            +++ "b/unic\303\270\342\210\202e\314\201.txt"
            @@ -0,0 +1,13 @@
            +μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος
            +οὐλομένην, ἣ μυρί᾽ Ἀχαιοῖς ἄλγε᾽ ἔθηκε,
            +πολλὰς δ᾽ ἰφθίμους ψυχὰς Ἄϊδι προΐαψεν
            """).strip()

        self._set_git_diff_output(diff_str, "", "")
        # Get the lines changed in the diff
        lines_changed = self.diff.lines_changed('unic\303\270\342\210\202e\314\201.txt')

        # Expect that three lines changed
        self.assertEqual(len(lines_changed), 3)


            master_diff = {0}
            staged_diff = {1}
            unstaged_diff = {2}