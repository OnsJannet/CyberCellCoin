import React from 'react'
import Icon1 from '../../images/svg-1.svg'
import Icon2 from '../../images/svg-2.svg'
import Icon3 from '../../images/svg-3.svg'
import {TeamContainer,
        TeamH1,
        TeamH2,
        TeamWrapper,
        TeamIcon,
        TeamP,
        TeamCard}
from './TeamElements'

const Team = () => {
    return (
        <TeamContainer id="team">
            <TeamH1>Our Team</TeamH1>
                <TeamWrapper>
                <TeamCard>
                    <TeamIcon src={Icon1}/>
                    <TeamH2> Abderrahmen Hidoussi</TeamH2>
                    <TeamP> BackEnd</TeamP>
                </TeamCard>
                <TeamCard>
                    <TeamIcon src={Icon2}/>
                    <TeamH2> Aymen Haddeji</TeamH2>
                    <TeamP> BackEnd</TeamP>
                </TeamCard>
                <TeamCard>
                    <TeamIcon src={Icon3}/>
                    <TeamH2>Ons Jannet</TeamH2>
                    <TeamP> FrontEnd</TeamP>
                </TeamCard>
            </TeamWrapper>
            
        </TeamContainer>
    )
}

export default Team
