import styled from "styled-components";

export const LandingWrapper = styled.div`
    width: 100%;
    height: 100%;
    max-width: 50rem;
    
    display: grid;
    gap: 2rem;

    margin: auto;
    padding: 2rem;
    box-sizing: border-box;

    background-color: var(--bg-secondary-color);
`

export const LandingHeader = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-height: 40rem;
    gap: 1rem;
`

export const LandingImg = styled.img`
    max-width: 50%;
    height: auto;
`

export const LandingTaglines = styled.div`
    text-align: end;
    display: flex;

    flex-direction: column;
    gap: 1rem;
`

export const LandingDesc = styled.div`
    display: flex;
    flex-direction: column;
    gap: 1rem;
`

export const LandingFooter = styled.div`
    max-width: 40%;
    width: 20rem;
    align-self: flex-end;
    justify-self: end;
`