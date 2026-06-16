---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_hti_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_hti_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_hti_2017
dataset_id: rdls_lss-hti_wfp_integratedcontextanalysis_2017
description: 'The ICA is a process of consultations supported by mapped-out data that
  produces a strategic plan describing where different combinations of programme themes
  are appropriate to achieve goals of reducing food insecurity and climate related
  shock risk. The ICA combines multi-year food security trends with natural shock
  risk data to highlight sub-national areas where different programme strategies make
  sense. Food security trend maps shows areas where safety nets can address regular
  food insecurity, and others where shocks make recovery more important. Climate-related
  natural shock risk maps show where DRR, preparedness and early warning efforts can
  complement food-security objectives. Atop this core foundation, mapped data on subjects
  including nutrition, gender, livelihoods and resilience can enrich theme-level strategic
  planning in which all pieces work together. The full group of ICA partners discuss
  these analytical results to arrive at strategic programmatic directions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_hti_2017]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trends (2007-2016) with historical
    natural shock occurrence data (1998-2010) and land degradation trends (2001-2012)
    to produce sub-national risk maps. Data were processed through consultations and
    geographic information analysis to identify areas where different combinations
    of food security and climate-related shock risks warrant targeted programme interventions.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_hti_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by flood risk
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by cyclone risk
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by landslide risk
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought risk
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ observed during the Integrated Context Analysis (ICA) run in Haiti in 2017.\
    \ Data source: NASA MODIS, 2001-2012. The key indicators used for the analysis\
    \ were the average ecological changes observed between 2001 and 2012 and the percentage\
    \ of erosion-prone surface. Cette couche contient les donn\xE9es necessaires pour\
    \ d\xE9terminer le niveau de d\xE9gradation de terres observ\xE9 pendant l'Analyse\
    \ Integr\xE9e de Contexte (AIC) effectu\xE9e en Haiti en 2017. Source des donn\xE9\
    es: NASA MODIS, 2001-2012. Les indicateurs principaux utilis\xE9s pour l'analyse\
    \ \xE9taient les changements moyens de couverture du sol observ\xE9s entre 2001et\
    \ 2012 et la pourcentage de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d7ba94db6d174ab8b13010d824efabab/data
  format: null
  id: resource_96269d84
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the rapid on-set shocks risk\
    \ (floods, landslides and cyclones) estimated during the Integrated Context Analysis\
    \ (ICA) run in Haiti in 2017. Data source: MultiRisk Analysis using 1998-2010\
    \ data, realized by WFP with OCHA and CNIGS in 2014. This analysis is part of\
    \ the 'Analysis of Multiple Natural Hazards in Haiti (NATHAT)'. Cette couche contient\
    \ informations regard le risque de chocs de d\xE9clenchement rapide (inondations,\
    \ glissements de terrain et cyclones) estim\xE9 pendant l'Analyse Integr\xE9e\
    \ du Contexte (AIC) effectu\xE9e en Haiti en 2017. Source des donn\xE9es: Analyse\
    \ Multi Risque, 1998-2010, realis\xE9e par le PAM avec OCHA et CNIGS en 2014.\
    \ L'analyse fait partie du document 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d0407d134c2d4bf18efb3c29357c886f/data
  format: null
  id: resource_c8002729
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Rapid On-Set Shocks Risk, 1998-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the recurrence of food insecurity\
    \ estimated during the Integrated Context Analysis (ICA) run in Haiti in 2017.\
    \ Data source: Data consolidated in WFP Haiti CO in 2017, originally collected\
    \ as part of 5 food security assessments performed between 2007 and 2016, result\
    \ of the collaboration of several organizations. The key indicator used for the\
    \ analysis was the Food Consumption Score (FCS) with a threshold set to 20%, considering\
    \ that this is the standard threshold used in the food insecurity classifications,\
    \ IPC included. Cette couche contient informations regard la r\xE9currence d'ins\xE9\
    curit\xE9 alimentaire estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ effectu\xE9e en Haiti en 2017. Source des donn\xE9es: donn\xE9es consolid\xE9\
    es par Bureau pays du PAM Haiti en 2017, initialement rassembl\xE9es \xE0 partir\
    \ des 5 enqu\xEAtes d'ins\xE9curit\xE9 alimentaire men\xE9es dans le pays, entre\
    \ 2007 et 2016, par nombreuses organizations. L'indicateur principal utilis\xE9\
    \ pour l'analyse \xE9tait le score de consommation alimentaire, avec un seuil\
    \ d'ins\xE9curit\xE9 alimentaire fix\xE9 \xE0 20%, compte tenu du fait que c'est\
    \ le seuil standard utilis\xE9 dans les classifications d'ins\xE9curit\xE9 alimentaire,\
    \ y compris l'IPC"
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5e226b4bcc1e417e9e3c1cd86adca997/data
  format: null
  id: resource_c9a7ee43
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Recurrence of Food Insecurity
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the combined natural shocks\
    \ risk (floods, landslides, cyclones and drought) estimated during the Integrated\
    \ Context Analysis (ICA) run in Haiti in 2017. Data source: MultiRisk Analysis\
    \ using 1998-2010 data, realized by WFP with OCHA and CNIGS in 2014. This analysis\
    \ is part of the 'Analysis of Multiple Natural Hazards in Haiti (NATHAT)'. Cette\
    \ couche contient informations regard le risque combin\xE9 des chocs naturels\
    \ (inondations, glissements de terrain, cyclones et s\xE8cheresse) estim\xE9 pendant\
    \ l'Analyse Integr\xE9e du Contexte (AIC) effectu\xE9e en Haiti en 2017. Source\
    \ des donn\xE9es: Analyse Multi Risque, 1998-2010, realis\xE9e par le PAM avec\
    \ OCHA et CNIGS en 2014. L'analyse fait partie du document 'Analysis of Multiple\
    \ Natural Hazards in Haiti (NATHAT)'."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/77aaf9e4ffab4eb9848dbef1007cb716/data
  format: null
  id: resource_2d2bc681
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Natural Shocks Risk, 1998-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food insecure population\
    \ figures estimated during the Integrated Context Analysis (ICA) run in Haiti\
    \ in 2017. Data source: 5 food security assessments, performed between 2007 and\
    \ 2016, with the contribution of several organizations. Cette couche contient\
    \ informations regard le nombre de personnes en situation d'ins\xE9curit\xE9 alimentaire\
    \ estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC) effectu\xE9e en Haiti\
    \ en 2017. Source des donn\xE9es: 5 enqu\xEAtes d'ins\xE9curit\xE9 alimentaire,\
    \ men\xE9es entre 2007 et 2016, par nombreuses organizations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7fd54461f52e499d8ad32b0e4cede863/data
  format: null
  id: resource_ca768e89
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Estimated Numbers of Food Insecure People, 2007-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final classification resulting\
    \ from the Integrated Context Analysis (ICA) run in Haiti in 2017, showing areas\
    \ of convergence between high recurrence of food insecurity and propensity to\
    \ natural shocks. Cette couche contient informations regard la classification\
    \ finale result\xE9e par l'Analyse Integr\xE9e du Contexte (AIC) effectu\xE9e\
    \ en Haiti en 2017, montrant les zones de convergence des niveaux \xE9lev\xE9\
    s de r\xE9currence d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/23b701ceb17d49599a05edea8676e2bb/data
  format: null
  id: resource_83215d85
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains the nine main livelihood zones identified and\
    \ used during the Integrated Context Analysis (ICA) run in Haiti in 2017. Data\
    \ source: Fewsnet, 2014. Cette couche contient les huit zones de moyens d'existence\
    \ identifi\xE9es et utilis\xE9es pendant l'Analyse Integr\xE9e de Contexte (AIC)\
    \ effectu\xE9e en Haiti en 2017. Source des donn\xE9es: Fewsnet, 2014."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bd40d00444f7437894567ce326c76661/data
  format: null
  id: resource_a11fc864
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Livelihood Zones, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk estimated during\
    \ the Integrated Context Analysis (ICA) run in Haiti in 2017. Data source: MultiRisk\
    \ Analysis using 1998-2010 data, realized by WFP with OCHA and CNIGS in 2014.\
    \ This analysis is part of the 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'. The key indicator used for the analysis was the number of documented\
    \ drought events recorded during the 20th century. Cette couche contient informations\
    \ regard le risque de s\xE8cheresse estim\xE9 pendant l'Analyse Integr\xE9e du\
    \ Contexte (AIC) effectu\xE9e en Haiti en 2017. Source des donn\xE9es: Analyse\
    \ Multi Risque, 1998-2010, realis\xE9e par le PAM avec OCHA et CNIGS en 2014.\
    \ L'analyse fait partie du document 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'. L'indicateur principal utilis\xE9 pour l'analyse \xE9tait le nombre\
    \ de temp\xEAtes/cyclones lequels ont eu lieu en le vingti\xE8me si\xE8cle."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c7e7aa794e1746c7a56fca5b84ecbba1/data
  format: null
  id: resource_101423da
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Drought Risk, 1998-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the cyclone risk estimated during\
    \ the Integrated Context Analysis (ICA) run in Haiti in 2017. Data source: MultiRisk\
    \ Analysis using 1998-2010 data, realized by WFP with OCHA and CNIGS in 2014.\
    \ This analysis is part of the 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'. The key indicators used for the analysis was the cyclone hazard score;\
    \ considering the technical expertise and knowledge of the experts involved in\
    \ the ICA process at the CO, the Nord-Ouest department has been reclassified from\
    \ Low to High due to the possible wind effects. Cette couche contient informations\
    \ regard le risque de temp\xEAtes/cyclones estim\xE9 pendant l'Analyse Integr\xE9\
    e du Contexte (AIC) effectu\xE9e en Haiti en 2017. Source des donn\xE9es: Analyse\
    \ Multi Risque, 1998-2010, realis\xE9e par le PAM avec OCHA et CNIGS en 2014.\
    \ L'analyse fait partie du document 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'. Compte tenu de l'expertise technique et de la conaissance du personnel\
    \ au CO, le d\xE9partment du Nord-Ouest a \xE9t\xE9 reclassifi\xE9 de faible \xE0\
    \ \xE9lev\xE9 en raison des possibles effets du vent."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/40b9571063fa4c47a4e0e08cd6f0c776/data
  format: null
  id: resource_0658a8ce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Cyclone Risk, 1998-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the landslide risk estimated\
    \ during the Integrated Context Analysis (ICA) run in Haiti in 2017. Data source:\
    \ MultiRisk Analysis using 1998-2010 data, realized by WFP with OCHA and CNIGS\
    \ in 2014. This analysis is part of the 'Analysis of Multiple Natural Hazards\
    \ in Haiti (NATHAT)'. The indicators used for the analysis were slope deficit,\
    \ instability, deformation, breaking and propagation potential and drainage systems.\
    \ Cette couche contient informations regard le risque de glissements de terraine\
    \ estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC) effectu\xE9e en Haiti\
    \ en 2017. Source des donn\xE9es: Analyse Multi Risque, 1998-2010, realis\xE9\
    e par le PAM avec OCHA et CNIGS en 2014. L'analyse fait partie du document 'Analysis\
    \ of Multiple Natural Hazards in Haiti (NATHAT)'. Les indicateurs principaux utilis\xE9\
    s pour l'analyse \xE9taient le d\xE9ficit de pente, instabilit\xE9, d\xE9formation,\
    \ rupture et propagation et la m\xE9thode de filtrage."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2e5f9211f4b549f6aa7ab936109eb58d/data
  format: null
  id: resource_7fef213d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Landslide Risk, 1998-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk estimated during\
    \ the Integrated Context Analysis (ICA) run in Haiti in 2017. Data source: MultiRisk\
    \ Analysis using 1998-2010 data, realized by WFP with OCHA and CNIGS in 2014.\
    \ This analysis is part of the 'Analysis of Multiple Natural Hazards in Haiti\
    \ (NATHAT)'. The indicators used for the analysis were the surface of the flooded\
    \ areas, flood frequency, flood depth, Digital Elevation Model (DEM), land typology\
    \ (hydrogeology and geology) and drainage systems. Cette couche contient informations\
    \ regard le risque d'inondations estim\xE9 pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) effectu\xE9e en Haiti en 2017. Source des donn\xE9es: Analyse Multi Risque,\
    \ 1998-2010, realis\xE9e par le PAM avec OCHA et CNIGS en 2014. L'analyse fait\
    \ partie du document 'Analysis of Multiple Natural Hazards in Haiti (NATHAT)'.\
    \ Les indicateurs principaux utilis\xE9s pour l'analyse \xE9taient les zones d'inondations,\
    \ la r\xE9currence d'inondations, la profondeur des inondations, le Digital Elevation\
    \ Model (DEM), la typologie du sol (hydrog\xE9ologie et g\xE9ologie) et le r\xE9\
    seau de drainage."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3a4348124d384da7903cb8975f21d0ec/data
  format: null
  id: resource_c91dd944
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Haiti, 2017 - Flood Risk, 1998-2010
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Haiti: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---
