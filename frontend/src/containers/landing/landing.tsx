import { LandingDesc, LandingFooter, LandingHeader, LandingImg, LandingTaglines, LandingWrapper } from "./landing.styles";
import Button from "../../components/button/button";
import { Heading, Paragraph, SubTitle } from "../../components/index.styles";

import logo_long from '../../assets/logo/logo_long.webp'

export default function Landing() {
    return (
        <LandingWrapper>
            <LandingHeader>
                <LandingImg 
                    src={logo_long}
                    alt="logo" 
                />
                <LandingTaglines>
                    <Heading>Tell <span className="italic">Us</span> Tales</Heading>
                    <Heading><span className="italic">We</span> Tales</Heading>
                    <Heading>Tally <span className="italic">Us</span> Tales</Heading>
                </LandingTaglines>
            </LandingHeader>
            <LandingDesc>
                <Paragraph>Hello <span className="sec-color">Unknown Traveller,</span></Paragraph>
                <SubTitle>Welcome to <span className="italic">TallyTale</span>, the ultimate destination for interactive storytelling! <span className="italic">TallyTale</span> redefines the way stories are created and enjoyed by transforming passive reading into an engaging, collaborative adventure. Whether you're a <span className="utl-color">seasoned writer</span> or an <span className="utl-color">enthusiastic reader</span>, <span className="italic">TallyTale</span> offers a unique platform where creativity and community come together to craft unforgettable tales.</SubTitle>
            </LandingDesc>
            <LandingFooter>
                <Button onClick={() => {}}>Soon</Button>
            </LandingFooter>
        </LandingWrapper>
    )
}