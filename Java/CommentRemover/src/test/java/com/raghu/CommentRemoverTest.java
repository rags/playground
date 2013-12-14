package com.raghu;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Maps;
import com.google.common.io.CharSource;
import com.google.common.io.CharStreams;
import org.junit.Test;

import java.io.File;
import java.io.InputStreamReader;

import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.junit.Assert.assertThat;


public class CommentRemoverTest {
    @Test
    public void shouldRemoveComments() throws Exception {
        ImmutableMap<String, String> map = ImmutableMap.of("greeglut.h", "greeglut_no-comment.h",
                "gtest-death-test.cc", "gtest-death-test_no-comment.cc",
                "mySample.cpp", "mySample_no-comment.cpp"
        );
        CommentRemover commentRemover = new CommentRemover();
        for (String input : map.keySet()) {
            commentRemover.removeComments(new File(CommentRemover.class.getResource(input).getPath()));
            String contents = CharStreams.toString(new InputStreamReader(CommentRemoverTest.class.getResourceAsStream(map.get(input))));
            assertThat(contents.replaceAll("\"[^\"]*\"", "\"\""),allOf(not(containsString("//")), not(containsString("/*"))));
        }

    }
}
