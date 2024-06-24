import styled from "styled-components";

export const InputWrapper = styled.div`
    width: 100%;
    box-sizing: border-box;

    font-size: 1.3em;
    border-radius: 1.4rem 0.7rem;

    display: flex;
    flex-direction: column;
    gap: 0.5rem;
`

export const InputHeader = styled.div`
    display: flex;
    justify-content: space-between;
    
    gap: 0.5rem;
    font-size: 0.9em;
`

export const InputLabel = styled.div`
    color: var(--txt-secondary-color);
`

export const InputError = styled.div`
    color: var(--utl-tertiary-color);
`

export const InputHighLight = styled.div`
    color: var(--utl-secondary-color);
`

export const InputField = styled.input`
    width: 100%;
    padding: 0.6rem 0.8rem;
    box-sizing: border-box;
    border: 1px solid #000;

    font-size: 1.1em;
    background-color: var(--bg-primary-color);
    color: var(--txt-primary-color);
`