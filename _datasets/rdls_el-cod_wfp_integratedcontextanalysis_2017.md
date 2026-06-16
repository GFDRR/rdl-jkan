---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_cod_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_cod_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_cod_2017
dataset_id: rdls_el-cod_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_cod_2017]'
details: null
exposure:
- asset_type:
    description: Population density distribution across Democratic Republic of Congo
      in 2015
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Livelihood zones and land degradation patterns (2001-2012) indicating
      agricultural exposure
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trends (2012-2017/2018) with
    natural shock hazard data (flood, landslide, rainfall variability) and population/livelihood
    exposure to identify sub-national areas where different programme strategies are
    appropriate for reducing food insecurity and climate shock risk. Hazard layers
    include observed flood and landslide maps (2013) and inter-annual rainfall variability
    (1981-2015), integrated with population density and livelihood zone data to assess
    vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_cod_2017
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence (2012-2017) as direct impact of drought
      and climate-related shocks on agricultural livelihoods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
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
    \ - by second-level administrative area - observed during the Integrated Context\
    \ Analysis (ICA) run in Democratic Republic of Congo in 2017. The analysis was\
    \ performed in three hot-spot provinces in the north-east part of the country\
    \ (Ituri, Nord-Kivu and Sud-Kivu) because of the recent conflict outbreak and\
    \ increasing food insecurity levels. Data source: HQ OSEP GIS Analysis of NASA\
    \ MODIS, 2001-2012 The main indicators used for the analysis were the average\
    \ ecological change observed within the time window considered and the percentage\
    \ of prone-erosion district surface. Cette couche contient les donn\xE9es necessaires\
    \ pour d\xE9terminer le niveau de d\xE9gradation de terres - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - observ\xE9 pendant l'Analyse Integr\xE9e de Contexte\
    \ (AIC) execut\xE9e en R\xE9publique D\xE9mocratique du Congo en 2017. Source\
    \ des donn\xE9es: HQ OSEP GIS Analyse de NASA MODIS, 2001-2012 Les indicateurs\
    \ principaux utilis\xE9s pour l'analyse \xE9taient les changements moyens de couverture\
    \ du sol observ\xE9s entre 2001 et 2012 et la pourcentage de surface ayant une\
    \ propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c9cf16a8a4544a6c80b2fe38eb610759/data
  format: null
  id: resource_a0fd2d95
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bdf4ade1927143cba4acb2d9d72cdc3a/data
  format: PNG
  id: resource_b7a51151
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Recurrence of Food Insecurity, 2012-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7247d977b443454aacc6719ead0b5a11/data
  format: PNG
  id: resource_55aa524b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Most Predominant Livelihood Zones,
    2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cdd9167b3f834ec5a5d8fc207f169a33/data
  format: PNG
  id: resource_57b90b9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - ICA Areas & Inter-annual Rainfall
    Variability (1981-2015)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/40b3881c28a24861a261b526274de7aa/data
  format: PNG
  id: resource_28cccb16
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Flood Hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d73dc32ae3aa4d269cda441d021d231b/data
  format: PNG
  id: resource_d05738b6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5e0cb04d1e1947f5a2a706fa0fbb7e80/data
  format: PNG
  id: resource_e1d30636
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Landslide Hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/89267b22b2ec44f7a3f62767054568b8/data
  format: PNG
  id: resource_0e13e53e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/37b753e12b9f4459b8778b97d26cf3ca/data
  format: PNG
  id: resource_cf762e9c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/698c076074a54fbda9c1338766eedb06/data
  format: PNG
  id: resource_69dbddba
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Natural Shock Hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/52b0647d09cf48e6baa76d14540f5e11/data
  format: PNG
  id: resource_a6a1c066
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - ICA Areas & Land Degradation (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the recurrence of food insecurity\
    \ - by second-level administrative area - observed during the Integrated Context\
    \ Analysis (ICA) run in Democratic Republic of Congo in 2017. The analysis was\
    \ performed in three hot-spot provinces in the north-east part of the country\
    \ (Ituri, Nord-Kivu and Sud-Kivu) because of the recent conflict outbreak and\
    \ increasing food insecurity levels. Data source: IPC 2012-2017. The main indicator\
    \ used for the analysis was the number of times that an IPC Phase 3 or above occurred\
    \ per each district, classified using terciles (Low = 0-33%; Medium = 33-66%;\
    \ High = 66-100%). Cette couche contient les donn\xE9es d'une analyse de tendance\
    \ de la s\xE9curit\xE9 alimentaire - par unit\xE9 administrative de deuxi\xE8\
    me niveau - employ\xE9e pendant l'Analyse Integr\xE9e de Contexte (AIC) ex\xE9\
    cut\xE9 en R\xE9publique D\xE9mocratique du Congo en 2017. L'analyse a \xE9t\xE9\
    \ execut\xE9e dans trois provinces critiques dans le secteur nord-est du pays\
    \ (Ituri, Nord-Kivu et Sud-Kivu) en raison du r\xE9cent d\xE9clenchement des conflits\
    \ et des croissants niveaux d'ins\xE9curit\xE9 alimentaire. Source des donn\xE9\
    es: IPC 2012-2017. L'indicateur principale utilis\xE9 pour l'analyse \xE9tait\
    \ le nombre de fois qu'il y a eu une phase IPC 3 ou sup\xE9rieur en chaque cercle,\
    \ classifi\xE9s par terciles (Faible = 0-33%; Moyen = 33-66%; Elev\xE9 = 66-100%)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a283a7dc751147afa73b8478caf28a4a/data
  format: null
  id: resource_6c39d074
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Recurrence of Food Insecurity, 2012-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA),
    2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9017d0445d0d4235a7e094658f6c8be4/data
  format: PNG
  id: resource_25e145a8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Recurrence of Food Insecurity, EFSA
    2012-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Democratic Republic\
    \ of Congo in 2017. The analysis, using the Emergency Food Security Assessment\
    \ (EFSA) data from 2012 to 2018, integrates the results of the overall food security\
    \ analysis for what concerns the Sud-Kivu region. Ce document Excel contient l'analyse\
    \ sur l'insecurit\xE9 alimentaire utilis\xE9e aux fins de l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en R\xE9publique D\xE9mocratique du Congo en 2017.\
    \ L'analyse, en utilisant les Emergency Food Security Assessment (EFSA) donn\xE9\
    es du 2012 au 2018, int\xE9gre les r\xE9sultats de l'analyse globale sur l'ins\xE9\
    curit\xE9 alimentaire pour ce qui concerne la r\xE9gion de Sud-Kivu."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3bb808936d294f73a81c85c8aa601f19/data
  format: null
  id: resource_3275ec1b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Food Insecurity Recurrence Analysis
    (EFSA Lens)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final classification resulting\
    \ from the Integrated Context Analysis (ICA) - by second-level administrative\
    \ area - run in Democratic Republic of Congo in 2017. The analysis was performed\
    \ in three hot-spot provinces in the north-east part of the country (Ituri, Nord-Kivu\
    \ and Sud-Kivu) because of the recent conflict outbreak and increasing food insecurity\
    \ levels. The final categorization shows areas of convergence between high recurrence\
    \ of food insecurity and propensity to natural shocks. Cette couche contient informations\
    \ regard la classification finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte\
    \ (AIC) execut\xE9e en R\xE9publique D\xE9mocratique du Congo en 2017, montrant\
    \ les zones de convergence de niveaux elev\xE9s de r\xE9currence d'ins\xE9curit\xE9\
    \ alimentaire et propension aux chocs naturels. L'analyse a \xE9t\xE9 execut\xE9\
    e dans trois provinces critiques dans le secteur nord-est du pays (Ituri, Nord-Kivu\
    \ et Sud-Kivu) en raison du r\xE9cent d\xE9clenchement des conflits et des croissants\
    \ niveaux d'ins\xE9curit\xE9 alimentaire."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ea6fc1a3332a4c09a5b2610d2b826203/data
  format: null
  id: resource_f06644d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the most predominant livelihood\
    \ zone - by second-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Democratic Republic of Congo in 2017. The analysis\
    \ was performed in three hot-spot provinces in the north-east part of the country\
    \ (Ituri, Nord-Kivu and Sud-Kivu) because of the recent conflict outbreak and\
    \ increasing food insecurity levels. Data source: Fewsnet, 2016. Cette couche\
    \ contient informations regard le zones de moyens d'existence plus pr\xE9dominant\
    \ - par unit\xE9 administrative de deuxi\xE8me niveau - identifi\xE9s pendant\
    \ l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en R\xE9publique D\xE9mocratique\
    \ du Congo en 2017. L'analyse a \xE9t\xE9 execut\xE9e dans trois provinces critiques\
    \ dans le secteur nord-est du pays (Ituri, Nord-Kivu et Sud-Kivu) en raison du\
    \ r\xE9cent d\xE9clenchement des conflits et des croissants niveaux d'ins\xE9\
    curit\xE9 alimentaire. Source des donn\xE9es: Fewsnet, 2016."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/66b7de4eb95b41c3852589e751441bd0/data
  format: null
  id: resource_37a72be6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Most Predominant Livelihood Zones,
    2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Democratic Republic\
    \ of Congo in 2017. The analysis, using the Integrated Phase Classification (IPC)\
    \ data from 2012 to 2017, determines the recurrence - by second-level administrative\
    \ area - of IPC Phases 3 or above. Ce document Excel contient l'analyse sur l'insecurit\xE9\
    \ alimentaire utilis\xE9e aux fins de l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en R\xE9publique D\xE9mocratique du Congo en 2017. L'analyse, en\
    \ utilisant les Integrated Phase Classification (IPC) donn\xE9es du 2012 au 2017,\
    \ d\xE9termine la r\xE9currence - par unit\xE9 administrative de deuxi\xE8me niveau\
    \ - de IPC Phase 3 ou au-dessus."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/acc1e3cde8c949ed9488098ea9486369/data
  format: null
  id: resource_16502c84
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the interannual rainfall variability\
    \ estimated during the Integrated Context Analysis (ICA) run in Democratic Republic\
    \ of Congo in 2017. The analysis was performed in three hot-spot provinces in\
    \ the north-east part of the country (Ituri, Nord-Kivu and Sud-Kivu) because of\
    \ the recent conflict outbreak and increasing food insecurity levels. Data source:\
    \ HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE), 1981-2015. The main indicator\
    \ used for the analysis was the maximum percentage of rainfall variability compared\
    \ to the long-term average. Cette couche contient informations regard la variabilit\xE9\
    \ interannulle des pr\xE9cipitations estim\xE9e pendant l'Analyse Integr\xE9e\
    \ du Contexte (AIC) execut\xE9e en R\xE9publique D\xE9mocratique du Congo en 2017.\
    \ L'analyse a \xE9t\xE9 execut\xE9e dans trois provinces critiques dans le secteur\
    \ nord-est du pays (Ituri, Nord-Kivu et Sud-Kivu) en raison du r\xE9cent d\xE9\
    clenchement des conflits et des croissants niveaux d'ins\xE9curit\xE9 alimentaire.\
    \ Source des donn\xE9s: HQ VAM Analyse de CHIRPS estimations des pr\xE9cipitations,\
    \ 1981-2015. L'indicateur principal utilis\xE9 pour l'analyse \xE9tait la pourcentage\
    \ maxime de variabilit\xE9 par rapport \xE0 la moyenne \xE0 long terme."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4d19013043344449b8cc0319c6086a94/data
  format: null
  id: resource_77f237b1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Inter-annual Rainfall Variability,
    1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood hazard estimated -\
    \ by second-level administrative area - during the Integrated Context Analysis\
    \ (ICA) run in Democratic Republic of Congo in 2017. The analysis was performed\
    \ in three hot-spot provinces in the north-east part of the country (Ituri, Nord-Kivu\
    \ and Sud-Kivu) because of the recent conflict outbreak and increasing food insecurity\
    \ levels. Data source: UNEP/UNISDR GAR 2013, EMDAT 1990-2016. The main indicators\
    \ used for the analysis were the percentage of district surface at flood hazard,\
    \ the maximum expected frequency of flood events and the number of flood events\
    \ recorded by EMDAT between 1990 and 2017. Cette couche contient informations\
    \ regard le risque d'inondations - par unit\xE9 administrative de deuxi\xE8me\
    \ niveau - estim\xE9 pendant l'Analyse Integr\xE9e de Contexte (AIC) ex\xE9cut\xE9\
    \ en R\xE9publique D\xE9mocratique du Congo en 2017. L'analyse a \xE9t\xE9 execut\xE9\
    e dans trois provinces critiques dans le secteur nord-est du pays (Ituri, Nord-Kivu\
    \ et Sud-Kivu) en raison du r\xE9cent d\xE9clenchement des conflits et des croissants\
    \ niveaux d'ins\xE9curit\xE9 alimentaire. Sources des donn\xE9es: UNEP/UNISDR\
    \ GAR 2013. Les indicateurs principales utilis\xE9s pour l'analyse \xE9taient\
    \ la pourcentage de surface \xE0 risque d'inondation et la combination de l'attente\
    \ maximale attendue des inondations selon UNEP/UNISDR et l'attente des inondations\
    \ enregistr\xE9es par EMDAT entre 1990 et 2016."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/be6c34c2c8d54b6094006c47baef03f1/data
  format: null
  id: resource_61f26e2d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Flood Hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the landslide hazard estimated\
    \ - by second-level administrative area - during the Integrated Context Analysis\
    \ (ICA) run in Democratic Republic of Congo in 2017. The analysis was performed\
    \ in three hot-spot provinces in the north-east part of the country (Ituri, Nord-Kivu\
    \ and Sud-Kivu) because of the recent conflict outbreak and increasing food insecurity\
    \ levels. Data source: UNEP/UNISDR GAR 2013. The main indicators used for the\
    \ analysis were the percentage of district surface at landslide hazard, the maximum\
    \ expected frequency of landslide events. Cette couche contient informations regard\
    \ le risque des glissements de terraine - par unit\xE9 administrative de deuxi\xE8\
    me niveau - estim\xE9 pendant l'Analyse Integr\xE9e de Contexte (AIC) ex\xE9cut\xE9\
    \ en R\xE9publique D\xE9mocratique du Congo en 2017. L'analyse a \xE9t\xE9 execut\xE9\
    e dans trois provinces critiques dans le secteur nord-est du pays (Ituri, Nord-Kivu\
    \ et Sud-Kivu) en raison du r\xE9cent d\xE9clenchement des conflits et des croissants\
    \ niveaux d'ins\xE9curit\xE9 alimentaire. Sources des donn\xE9es: UNEP/UNISDR\
    \ GAR 2013. Les indicateurs principales utilis\xE9s pour l'analyse \xE9taient\
    \ la pourcentage de surface \xE0 risque des glissements de terraine et l'attente\
    \ maximale attendue des glissements de terraine."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/93ac11371b9b4826ac5b3aa922f82df8/data
  format: null
  id: resource_f6d56b2b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Landslide Hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the combined natural shock (floods\
    \ and landslides) hazard estimated - by second-level administrative area - during\
    \ the Integrated Context Analysis (ICA) run in Democratic Republic of Congo in\
    \ 2017. The analysis was performed in three hot-spot provinces in the north-east\
    \ part of the country (Ituri, Nord-Kivu and Sud-Kivu) because of the recent conflict\
    \ outbreak and increasing food insecurity levels. Data source: UNEP/UNISDR GAR\
    \ 2013, EMDAT 1990-2016. Cette couche contient informations regard le risque des\
    \ chocs naturals combin\xE9s (inondations, et glissements de terrain) - par unit\xE9\
    \ administrative de deuxi\xE8me niveau - estim\xE9 pendant l'Analyse Integr\xE9\
    e de Contexte (AIC) execut\xE9 en R\xE9publique D\xE9mocratique du Congo en 2017.\
    \ L'analyse a \xE9t\xE9 execut\xE9e dans trois provinces critiques dans le secteur\
    \ nord-est du pays (Ituri, Nord-Kivu et Sud-Kivu) en raison du r\xE9cent d\xE9\
    clenchement des conflits et des croissants niveaux d'ins\xE9curit\xE9 alimentaire.\
    \ Source des donn\xE9es: UNEP/UNISDR GAR 2013, EMDAT 1990-2016."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1bda0604084349f09dfb67f2c987d1d5/data
  format: null
  id: resource_9b1a3361
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Natural Shock Hazard
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cod_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---
