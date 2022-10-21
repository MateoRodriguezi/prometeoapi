
import Foooter from "components/navigation/Footer"
import NavBar from "components/navigation/NavBar"
import { connect } from "react-redux"


const FullWidthLayout = ({children}) => {
    return(
        <>
        <NavBar/>
        {children}
        <Foooter/>
        </>
    )
}

const mapStateToProps = state =>({

})

export default connect(mapStateToProps,{

})(FullWidthLayout)