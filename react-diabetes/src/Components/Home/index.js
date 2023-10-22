import "./index.scss"
import { Link } from 'react-router-dom';
import Globe from "../../assets/Globe.png"

const Home = () => {
    return (
        <>
            <div className="container home-page">
                <div className="title">
                Small sicknesses sneaking into your everyday?
                </div>
                <div className="subtitle">What if those minor discomforts are a sign of something major?</div>
                <div className="globe"><img src={Globe} alt ="globe"/></div>
            </div>
        </>
    )
}

export default Home