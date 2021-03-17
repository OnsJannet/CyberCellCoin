import React from 'react'
import Icon1 from '../../images/svg-1.svg'
import Icon2 from '../../images/svg-2.svg'
import Icon3 from '../../images/svg-3.svg'
import {TeamContainer,
        TeamH1,
        TeamWrapper,
        TeamCard,
        TeamIcon,
        TeamH2,
        TeamP
        } from './TeamElements';

const Team= () => {
    return (
        <TeamContainer id="team">
            <TeamH1>Our Team</TeamH1>
            <TeamWrapper>
                <TeamCard>
                <TeamIcon src={Icon1}/>
                <TeamH2> Abdou</TeamH2>
                <TeamP> Backend Developer </TeamP>
                </TeamCard>
                <TeamCard>
                <TeamIcon src={Icon2}/>
                <TeamH2> Aymen</TeamH2>
                <TeamP> Backend Developer </TeamP>
                </TeamCard>
                <TeamCard>
                <TeamIcon src={Icon3}/>
                <TeamH2> Ons</TeamH2>
                <TeamP> Frontend Developer </TeamP>
                </TeamCard>
            </TeamWrapper>   
        </TeamContainer>
    );
};
export default Team
