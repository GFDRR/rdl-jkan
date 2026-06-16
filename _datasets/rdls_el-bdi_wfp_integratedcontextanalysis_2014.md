---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_bdi_2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_bdi_2014
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_bdi_2014
dataset_id: rdls_el-bdi_wfp_integratedcontextanalysis_2014
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_bdi_2014]'
details: null
exposure:
- asset_type:
    description: Projected population distribution across Burundi in 2013
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
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend analysis with natural
    shock risk data (flood and landslide hazard maps from 2009-2015) and projected
    population distribution to identify sub-national areas where different programme
    strategies are appropriate for reducing food insecurity and climate shock vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_bdi_2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure to flood risk in Burundi 2012-2015
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposure to landslide risk in Burundi
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2b38859b8c5a4e75b3114065846a1fa8/data
  format: PNG
  id: resource_a6cb2cfd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Flood Risk, 2012-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cd5c4f921cb048dfbb9886e6aed1b87d/data
  format: PNG
  id: resource_27bb173b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by livelihood\
    \ zone - estimated during the Integrated Context Analysis (ICA) run in Burundi\
    \ between 2014 and 2015. Data source: Strategie Nationale de Pr\xE9vention des\
    \ Risques et de Gestion des Catastrophes - Plan d'Action National, 2012-2015.\
    \ The key indicator used for the analysis was a descriptive flood index, provided\
    \ by the source with no information about the data and the methodology behind\
    \ it. Cette couche contient informations regard le risque d'inondations - par\
    \ zones de moyens d'existence - estim\xE9 pendant l'Analyse Integr\xE9e de Contexte\
    \ (AIC) ex\xE9cut\xE9 au Burundi entre 2014 et 2015. Sources des donn\xE9es: Strategie\
    \ Nationale de Pr\xE9vention des Risques et de Gestion des Catastrophes - Plan\
    \ d'Action National, 2012-2015. L'indicateur principale utilis\xE9 pour l'analyse\
    \ \xE9tait un index des inondations, fourni par la source avec pas des informations\
    \ regard les donn\xE9es utilis\xE9es ainsi que la m\xE9thodologie employ\xE9e."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/19837e18ef9f48bd9508a9d3098572e2/data
  format: null
  id: resource_3d249cd2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Flood Risk, 2012-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/442b4e6cd76d4beda7213049969c67e8/data
  format: PNG
  id: resource_a84648e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) run in Burundi between 2014 and 2015,\
    \ showing areas of convergence between high levels of recurrence of food insecurity\
    \ and propensity to natural shocks. Cette couche contient informations regard\
    \ la classification finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC)\
    \ execut\xE9e au Burundi entre 2014 et 2015, montrant les zones de convergence\
    \ de niveaux elev\xE9s de r\xE9currence d'ins\xE9curit\xE9 alimentaire et propension\
    \ aux chocs naturels."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c7743d41e35c4ecc914d60c64dc4ebe7/data
  format: null
  id: resource_10bf9c62
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the projected population for\
    \ 2013 used in the Integrated Context Analysis (ICA) run in Burundi between 2014\
    \ and 2015. Data source: Burundi Census, 2008. Cette couche contient informations\
    \ regard la population projet\xE9e en 2013 utilis\xE9e pendant l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e au Burundi entre 2014 et 2015. Source des donn\xE9\
    es: Burundi Census, 2008"
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/eef06540581145099854799c44af0dd0/data
  format: null
  id: resource_b39bfb6f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Projected Population, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/69e70093524a4d4bb65cd15455430a39/data
  format: PNG
  id: resource_71b87626
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Projected Population, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fb4bf545e806471092355900cc2f4534/data
  format: PNG
  id: resource_332ea8b6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Landslide Risk, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/500119c8e2284723a48d87de6360daa8/data
  format: PNG
  id: resource_9d30e5f0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Areas & Prevalence of Stunting (2014)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/34f84e7434874ed692faf051c021f85d/data
  format: PNG
  id: resource_db51962b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Livelihood Zones, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f36162b54320495fa60353cd016e13c5/data
  format: PNG
  id: resource_8471527c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Areas, Prevalence of Stunting (2014) & High Population
    Density (2011)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Burundi between\
    \ 2014 and 2015. The analysis, using the Food Security Monitoring System (FSMS)\
    \ and Comprehensive Food Security and Vulnerability Assessment (CFSVA) data from\
    \ 2009 to 2014, determines the recurrence of food insecurity conditions - by livelihood\
    \ zone - applying a threshold equal to 30%. Ce document Excel contient l'analyse\
    \ sur l'insecurit\xE9 alimentaire utilis\xE9e aux fins de l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en Burundi entre 2014 et 2015. L'analyse, en utilisant\
    \ les Food Security Monitoring System (FSMS) and Comprehensive Food Security and\
    \ Vulnerability Assessment (CFSVA) donn\xE9es du 2009 au 2014, d\xE9termine la\
    \ r\xE9currence de conditions d'insecurit\xE9 alimentaire - par zone de moyens\
    \ d'existence. Le seuil de s\xE9curit\xE9 alimentaire (mesur\xE9 par le score\
    \ de consommation alimentaire pauvre et limite) est fix\xE9 \xE0 30%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2c6a3c1a00ce49ef95208aeca6b3ce86/data
  format: null
  id: resource_dad7d10c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Burundi between 2014 and 2015. The analysis brings together\
    \ the historical risk of natural shocks (floods, landslides and droughts) and\
    \ the recurrence of high food insecurity with other key contextual information\
    \ to provide broad programmatic strategies by livelihood zone. Ce document contient\
    \ les r\xE9sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e au Burundi entre 2014 et 2015. L'analyse rassemble le risque historique des\
    \ chocs naturels (inondations, glissements de terrain et s\xE8cheresse) et la\
    \ r\xE9currence elev\xE9e d'ins\xE9curit\xE9 alimentaire avec autres informations\
    \ contextuelles afin de fournir grandes strat\xE9gies programmatiques par zones\
    \ de moyens d'existence."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/93457536b9df4526bf877713e35c1b5c/data
  format: null
  id: resource_4cb4070f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/afe06eeb52b445daa55686a9ad1b32f8/data
  format: PNG
  id: resource_1a232baa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Rapid On-Set Shocks
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f9a42d2bbab24d7a9050c0004f4d5d80/data
  format: PNG
  id: resource_4dd41ea9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the combined natural shocks\
    \ risk (flood, landslides and droughts) - by livelihood zone - estimated during\
    \ the Integrated Context Analysis (ICA) run in Burundi between 2014 and 2015.\
    \ Data source: Strat\xE9gie Nationale de Pr\xE9vention des Risques et de Gestion\
    \ des Catastrophes - Plan d'Action National 2012-2015, UNEP/UNISDR GAR 2009, HQ\
    \ VAM Analysis of NDVI data 1999-2013. Cette couche contient informations regard\
    \ le risque des chocs naturals combin\xE9s (inondations, glissements de terrain\
    \ et s\xE8cheresse) - par zones de moyens d'existence - estim\xE9 pendant l'Analyse\
    \ Integr\xE9e de Contexte (AIC) execut\xE9 au Burundi entre 2014 et 2015. Source\
    \ des donn\xE9es: Strat\xE9gie Nationale de Pr\xE9vention des Risques et de Gestion\
    \ des Catastrophes - Plan d'Action National 2012-2015, UNEP/UNISDR GAR 2009, HQ\
    \ VAM Analyse de NDVI donn\xE9es."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/79eddd232a5e427b8a423f332b0fd1c2/data
  format: null
  id: resource_c0339f99
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by livelihood zone - observed during the Integrated Context Analysis (ICA)\
    \ run in Burundi between 2014 and 2015. Data source: ICPAC & Regional Centre for\
    \ Mapping of Resources for Development (RCMRD), 2011. The key indicator used for\
    \ the analysis was the percentage of surface affected by a high or very high level\
    \ of degradation. Cette couche contient les donn\xE9es necessaires pour d\xE9\
    terminer le niveau de d\xE9gradation de terres - par zones de moyens d'existence\
    \ - observ\xE9 pendant l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e au\
    \ Burundi entre 2014 et 2015. Source des donn\xE9es: ICPAC & RCMRD, 2011. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait la pourcentage de surface avec\
    \ une d\xE9gradation elev\xE9e ou tr\xE8s elev\xE9e."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6ee1615053a64cf5badced764492877b/data
  format: null
  id: resource_a80468da
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Land Degradation, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2f07d6af0a0c4646a39c01bcbd547961/data
  format: PNG
  id: resource_9cd36132
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Recurrence of Food Insecurity, 2009-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/97710d011f684c7f9319b3f9010e2750/data
  format: PNG
  id: resource_3ef9cf5c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Land Degradation, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f6a16471b143499bb35f86c5ee5a7a6a/data
  format: PNG
  id: resource_f7cb3d0c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Areas, Land Degradation & High Population Density
    (2011)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains the eight main livelihood zones identified and\
    \ used during the Integrated Context Analysis (ICA) run in Burundi between 2014\
    \ and 2015. Data source: FSMS, 2009. Cette couche contient les huit zones de moyens\
    \ d'existence identifi\xE9es pendant l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9\
    e au Burundi entre 2014 et 2015. Source des donn\xE9es: FSMS, 2009."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ba5c47307ffe4c9eb5cddce84352b4d9/data
  format: null
  id: resource_c25bd4f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Livelihood Zones, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by livelihood\
    \ zone - estimated during the Integrated Context Analysis (ICA) run in Burundi\
    \ between 2014 and 2015. Data source: HQ VAM Analysis of NDVI data, 1999-2013.\
    \ The key indicator used for the analysis was the number of poor growing seasons\
    \ during the time frame of interest. Cette couche contient informations regard\
    \ le risque de s\xE8cheresse - par zones de moyens d'existence - estim\xE9 pendant\
    \ l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9 au Burundi entre 2014 et\
    \ 2015. Source des donn\xE9es: HQ VAM Analyse de NDVI donn\xE9es, 1999-2013. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait le nombre de saison qui ont connu\
    \ un d\xE9ficit hydrique (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/67d7f2bb021843979e61cfe0e50d7c0c/data
  format: null
  id: resource_e2233689
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Drought Risk, 1999-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7eaccef246f4446a8fe619d50737f655/data
  format: PNG
  id: resource_b7c62215
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - ICA Areas & High Population Density (2011)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burundi: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/49113ff994344d8597b2946a18c96c61/data
  format: PNG
  id: resource_f272eed7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Drought Risk, 1999-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the rapid on-set shocks risk\
    \ (floods and landslides) - by livelihood zone - estimated during the Integrated\
    \ Context Analysis (ICA) run in Burundi between 2014 and 2015. Data source: Strat\xE9\
    gie Nationale de Pr\xE9vention des Risques et de Gestion des Catastrophes - Plan\
    \ d'Action National 2012-2015, UNEP/UNISDR GAR 2009. Cette couche contient informations\
    \ regard le risque de chocs de d\xE9clanchement rapide (inondations et glissements\
    \ de terrain) - par zones de moyens d'existence - estim\xE9 pendant l'Analyse\
    \ Integr\xE9e de Contexte (AIC) execut\xE9 au Burundi entre 2014 et 2015. Source\
    \ des donn\xE9es: Strat\xE9gie Nationale de Pr\xE9vention des Risques et de Gestion\
    \ des Catastrophes - Plan d'Action National 2012-2015, UNEP/UNISDR GAR 2009."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5f813fd3160d4188b144512ffee255f5/data
  format: null
  id: resource_8f499b38
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Rapid On-Set Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition status observed
    during the Integrated Context Analysis (ICA) run in Burundi between 2014 and 2015.
    Data source: Multiple Indicator Cluster Survey (MICS), 2014. The key indicator
    used for the analysis was the prevalence of stunting in children below 5 years
    of age.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b3c7ea2bc99f42e7bb72b7c57ba63670/data
  format: null
  id: resource_8caa6c47
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Prevalence of Stunting, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the recurrence of food insecurity\
    \ observed during the Integrated Context Analysis (ICA) run in Burundi between\
    \ 2014 and 2015. Data source: Food Security Monitoring System (FSMS) 2009-2013,\
    \ Comprehensive Food Security and Vulnerability Analysis (CFSVA-SMART) 2014. The\
    \ key indicator used for the analysis was the Food Consumption Score (FCS) with\
    \ a threshold set to 30%. Cette couche contient les donn\xE9es d'une analyse de\
    \ tendance de la s\xE9curit\xE9 alimentaire - par zones de moyens d'existence\
    \ - employ\xE9e pendant l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e au\
    \ Burundi entre 2014 et 2015. Source des donn\xE9es: FSMS 2009-2013, CFSVA-SMART\
    \ 2014. L'indicateur principale utilis\xE9 pour l'analyse \xE9tait le score de\
    \ consommation alimentaire des m\xE9nages, avec un seuil de 30% des m\xE9nages\
    \ enqu\xEAt\xE9s."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/36275914304e41f095ea835cfae20fb3/data
  format: null
  id: resource_0fb1c1a4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Recurrence of Food Insecurity, 2009-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the landslide risk - by livelihood\
    \ zone - estimated during the Integrated Context Analysis (ICA) run in Burundi\
    \ between 2014 and 2015. Data source: UNEP/UNISDR Global Assessment of Risk (GAR),\
    \ 2009. The key indicators used for the analysis were the maximum expected frequency\
    \ of landslide events and the percentage of surface affected by landslide risk.\
    \ Cette couche contient informations regard le risque de glissements de terrain\
    \ - par zones de moyens d'existence - estim\xE9 pendant l'Analyse Integr\xE9e\
    \ de Contexte (AIC) execut\xE9e au Burundi entre 2014 et 2015. Source des donn\xE9\
    es: UNEP/UNISDR GAR, 2009. Les indicateurs principales utilis\xE9s pour l'analyse\
    \ \xE9taient la fr\xE9quence maximale de glissements de terrain et la pourcentage\
    \ de surface \xE0 risque de glissements de terrain."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/963c4cb0a7524ba8823f47cc0c4013f8/data
  format: null
  id: resource_0f00c812
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burundi, 2014 - Landslide Risk, 2009
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bdi_wfp_integratedcontextanalysis_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: 'Burundi: Integrated Context Analysis (ICA), 2014'
version: null
vulnerability: null
---
