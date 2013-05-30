
  function aujourdui(){
		maintenant=new Date();
		jour=maintenant.getDate();
		mois=maintenant.getMonth()+1;
		an=maintenant.getFullYear();
		
		document.ajout_doc.elements[2].value=an.toString()+"-"+mois+"-"+jour;
		}
  function bon_format_date(chaine) {
	    var exp=new RegExp("^[0-9]{4}-[01]?[0-9]-[0-9]{1,2}$","g");
	    return exp.test(chaine);
	  }

  function verif_champs(){
	  //alert(parseInt((document.ajout_doc.nb_page.value)));
		//alert(bon_format_date(document.ajout_doc.date_publication.value));
	  if (document.ajout_doc.types_docs.value=="none"){
			alert("Choisissez un type de document valide!");
			return false;
		}
		if(document.ajout_doc.titre.value.length < 2){
			alert("Tapez un titre de document correct!");	
			return false;
		}
		if(isNaN(document.ajout_doc.nb_page.value)){
			alert("Le nombre de pages saisie n\'est pas entier!");
			alert(parseInt((document.ajout_doc.nb_page.value)));
			return false;
		}
		if(isNaN(document.ajout_doc.nb_explaire.value)){
			alert("Le nombre d\'exemplaires saisi n\'est pas entier!");	
			return false;
		}
		if(bon_format_date(document.ajout_doc.date_publication.value)==false){
			alert("Le format de la date n'est pas correct!");	
					return false;
		}
		if(document.ajout_doc.types_docs.value=="pfe"){
		if((document.ajout_doc.nom_etd1.value.length < 2)||(document.ajout_doc.prenom_etd1.value.length < 2)){
			alert("Le nom ou prenom du premier étudiant est incorrect.");	
			return false;
		}
		if((document.ajout_doc.nom_encadrant.value.length < 2)||(document.ajout_doc.prenom_encadrant.value.length < 2)){
			alert("Le nom ou prenom de l\'encadrant est incorrect.");	
			return false;
		}
		
		if((document.ajout_doc.nom_etd2.value.length < 2)||(document.ajout_doc.prenom_etd2.value.length < 2)){
			alert("Le nom ou prenom du deuxième étudiant est incorrect.");	
			return false;
		}
		}//pfe
		if(document.ajout_doc.types_docs.value=="ouvrage"){
		if(isNaN(document.ajout_doc.isbn.value)){
			alert("L\'ISBN saisi n\'est pas entier!");	
			return false;
		}
		if(document.ajout_doc.auteur.value.length < 2){
			alert("Le nom de l\'auteur de l\'ouvrage est incorrect!");	
			return false;
		}
		if(document.ajout_doc.maison_ed.value.length < 2){
			alert("Tapez un nom de maison d\'édition correct!");	
			return false;
		}
		}//ouvrage
		if(document.ajout_doc.types_docs.value=="these"){
		if((document.ajout_doc.nom_encadrant.value.length < 2)||(document.ajout_doc.prenom_encadrant.value.length < 2)){
			alert("Le nom ou prenom de l\'encadrant est incorrect.");	
			return false;
		}
		
		if((document.ajout_doc.nom_etd.value.length < 2)||(document.ajout_doc.prenom_ed.value.length < 2)){
			alert("Le nom ou prenom de l\'étudiant est incorrect.");	
			return false;
		}
		if((document.ajout_doc.nom_jury.value.length < 2)||(document.ajout_doc.prenom_jury.value.length < 2)){
			alert("Le nom ou prenom du jury de thèse est incorrect.");	
			return false;
		}
		}//these
		return true;
  }
	

