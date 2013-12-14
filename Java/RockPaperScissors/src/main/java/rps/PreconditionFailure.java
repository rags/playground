package rps;

//raised when a pre-condition/invariant-check fails
public class PreconditionFailure extends RuntimeException{
    public PreconditionFailure(String message) {
        super(message);
    }
}
