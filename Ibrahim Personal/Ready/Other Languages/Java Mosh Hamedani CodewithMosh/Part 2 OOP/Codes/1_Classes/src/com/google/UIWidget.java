package com.google;

public interface UIWidget extends Draggable, Resizable { // here lets say we need all the capabilities in one place, hence we can use inheritance between the two interfaces.
    // note here that UIWidget is a child interface hence unlike classes Java Interface can have multiple parents
    // This is not a problem for Java interfaces which we say classes faces due to multiple inheritance because if this parents
    // declare the same method with the same signature this interface will inherit only one of them and also the imnplementation is defined
    // in a separate class hence there is no ambiguity

    void render();
}

