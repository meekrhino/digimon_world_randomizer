import * as React from 'react';
import * as ReactDOM from 'react-dom';
import * as path from "path";

import MainContainer from "./MainContainer";

namespace global {
	declare namespace JSX {
		interface ElementAttributesProperty extends Object { }
	}
}
//Render the main container into the html
ReactDOM.render( <MainContainer rootDirectory={__dirname + "/../"} />, document.getElementById( 'MainContainer' ) )
