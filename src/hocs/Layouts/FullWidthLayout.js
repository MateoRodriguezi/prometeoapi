
import Footer from "components/navigation/footer"
import NavBar from "components/navigation/NavBar"
import { connect } from "react-redux"


const FullWidthLayout = ({children}) => {
    return(
        <>
        <NavBar/>
        {children}
        <Footer/>
        </>
    )
}

const mapStateToProps = state =>({

})

export default connect(mapStateToProps,{

})(FullWidthLayout)