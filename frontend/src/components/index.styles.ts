import styled from "styled-components";

const TextWrapper = styled.p`
    color: var(--txt-primary-color);

    .italic {
        font-style: italic;
    }
    .sec-color {
        color: var(--txt-secondary-color);
    }
    .utl-color {
        color: var(--utl-primary-color);
    }
`

export const Heading = styled(TextWrapper)`
    font-size: 1.8em;

    @media only screen and (max-width: 990px) {
        font-size: 1.5em;
    }
`

export const Paragraph = styled(TextWrapper)`
    font-size: 1.6em;

    @media only screen and (max-width: 990px) {
        font-size: 1.4em;
    }
`

export const SubTitle = styled(TextWrapper)`
    font-size: 1.2em;
    letter-spacing: -0.02rem;
    word-spacing: 0.3rem;

    @media only screen and (max-width: 990px) {
        font-size: 1.1em;
    }
`