import React, {useState} from 'react';
import Video from '../../video/video.mp4';
import {Button} from '../ButtonElement';
import { HeroContainer, 
    HeroBg, 
    VideoBg, 
    HeroContent,
    HeroH1,
    HeroP,
    HeroBtnWrapper,
    ArrowForward,
    ArrowRight}
from './HeroElements';

const HeroSection = () => {
    const [hover, setHover] = useState(false)
    const onHover = () => {
        setHover(!hover);
    };

    return (
        <HeroContainer id="home">
            <HeroBg>
                <VideoBg autoPlay loop muted src={Video} type='video/mp4'/>
            </HeroBg>
            <HeroContent>
                <HeroH1> Trasactions Made Easy</HeroH1>
                <HeroP> 
                Cybercell is a degital asset designed to work as a medium of 
                exchange that uses strong cryptography to secure financial transactions, 
                control the creation of additional units, and verify the transfer of assets.
                </HeroP>
                <HeroBtnWrapper>
                    <Button 
                    to='signup' 
                    onMouseEnter={onHover} 
                    onMouseLeave={onHover}
                    primary='true' 
                    dark='true'
                    smooth={true} duration={500} spy={true} exact='true' offset={-80}
                    >
                        Get started {hover ? <ArrowForward /> : <ArrowRight />}
                    </Button>
                </HeroBtnWrapper>
            </HeroContent>        
        </HeroContainer>
    );
};

export default HeroSection;