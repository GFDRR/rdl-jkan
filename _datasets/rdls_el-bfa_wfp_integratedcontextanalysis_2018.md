---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_bfa_2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_bfa_2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_bfa_2018
dataset_id: rdls_el-bfa_wfp_integratedcontextanalysis_2018
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_bfa_2018]'
details: null
exposure:
- asset_type:
    description: Total population and population density estimates for 2015 and 2018
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
    description: Livelihood zones classified by predominant agricultural and pastoral
      activities
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trends (2014-2018) with natural
    shock risk data (drought 1981-2015, flood 2013, land degradation 2001-2012) and
    population estimates to identify sub-national areas where different programme
    strategies are appropriate. Food insecurity recurrence patterns are cross-referenced
    with hazard exposure to estimate vulnerable populations and shock-induced food
    insecurity impacts.
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
- href: https://data.humdata.org/dataset/wfp_ica_bfa_2018
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence linked to drought shocks over 2014-2018
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
  - asset_category: population
    asset_dimension: population
    description: Estimated numbers of food insecure people and additional vulnerable
      population in case of major drought shock
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/886472af5a254f169a640f6d850a3b2c/data
  format: PNG
  id: resource_7ef1e57e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by first-level administrative area - observed for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Burkina Faso in 2018. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data sources: HQ OSEP GIS Analyse des donn\xE9es NASA MODIS 2001-2012,\
    \ WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation Model. The main indicators\
    \ used for the analysis were the average ecological changes observed between 2001\
    \ and 2012 and the percentage of erosion-prone surface. Cette couche contient\
    \ les donn\xE9es necessaires pour determiner le niveau de d\xE9gradation des terres\
    \ - par unit\xE9 administrative de deuxi\xE8me niveau - observ\xE9 pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Burkina Faso en 2018. L'analyse\
    \ a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9\
    gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier\
    \ g\xE9n\xE9rale du PAM. Source des donn\xE9es: HQ OSEP GIS Analyse des donn\xE9\
    es NASA MODIS 2001-2012, WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation\
    \ Model. Les indicateurs principaux utilis\xE9s pour l'analyse \xE9taient les\
    \ changements moyens de couverture du sol observ\xE9s entre 2001 et 2012 et la\
    \ pourcentage de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a8a8ced13736469c8ad8448a58e25fc0/data
  format: null
  id: resource_8bf837df
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food security trend analysis\
    \ - by first-level administrative unit - used for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Burkina Faso in 2018. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Ministry of Agriculture and Food Security (MASA) 2014,\
    \ EPA 2015-2017 and Emergency Food Security Analysis (EFSA) 2018. The main indicator\
    \ used for the analysis was the CARI (Consolidated Approach to Reporting Indicators\
    \ of Food Security) indicator, with a threshold - referring to moderately and\
    \ severely food insecure households - set to 15%. Cette couche contient les donn\xE9\
    es d'une analyse de tendance de la s\xE9curit\xE9 alimentaire - par unit\xE9 administrative\
    \ de premi\xE8re niveau - employ\xE9e pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Ministry of Agriculture and Food Security (MASA) 2014, EPA 2015-2017\
    \ and Emergency Food Security Analysis (EFSA) 2018. L'indicateur principale utilis\xE9\
    \ pour l'analyse \xE9tait l'indicateur CARI (Consolidated Approach to Reporting\
    \ Indicators of Food Security), avec un seuil - mesur\xE9 par le menages en ins\xE9\
    curit\xE9 alimentaire mod\xE9r\xE9e et s\xE9v\xE8re - fix\xE9 \xE0 15%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6bb4e079ed1f4c5ba904f8fcc3d15f7f/data
  format: null
  id: resource_e3b70453
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Recurrence of Food Insecurity, 2014-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by first-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Burkina Faso in 2018. The analysis is a joint effort between the Regional\
    \ Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data source:\
    \ HQ VAM Analysis of Chirps Rainfall Estimates (RFE), 1981-2015. The main indicator\
    \ used for the analysis was the number of poor growing seasons observed in the\
    \ time window of interest. Cette couche contient informations regard le risque\
    \ de s\xE8cheresse - par unit\xE9 administrative de premi\xE8re niveau - estim\xE9\
    e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Burkina Faso\
    \ en 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre\
    \ le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme\
    \ au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: HQ VAM Analyse des\
    \ donn\xE9es CHIRPS d'estimation des precipitations, 1981-2015. L'indicateur principale\
    \ utilis\xE9 pour l'analyse \xE9tait le nombre de saisons qui ont connu un d\xE9\
    ficit hydrique (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3b24327fa8a448ddb0175cb0afd96b30/data
  format: null
  id: resource_c5afd220
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the malnutrition levels - by\
    \ first-level administrative unit - used for the purposes of the Integrated Context\
    \ Analysis (ICA) run in Burkina Faso in 2018. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and HQ GIS Unit and Programme division.\
    \ Data source: Standardized Monitoring and Assessment of Relief and Transitions\
    \ (SMART), 2013-2017 The main indicator used for the analysis was the prevalence\
    \ of Global Acute Malnutrition (GAM) and chronic Global Acute Malnutrition, with\
    \ thresholds set according to the guidelines suggested by the World Health Organization\
    \ (WHO). Cette couche contient informations regard les niveaux de malnutrition\
    \ - par unit\xE9 administrative de premi\xE8re niveau - observ\xE9s pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Burkina Faso en 2018. L'analyse\
    \ a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9\
    gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier\
    \ g\xE9n\xE9rale du PAM. Source des donn\xE9es: Standardized Monitoring and Assessment\
    \ of Relief and Transitions (SMART), 2013-2017 Les indicateurs principaux utilis\xE9\
    s pour l'analyse \xE9taient la pr\xE9valence de Malnutrition Aig\xFCe Globale\
    \ (MAG) et de Malnutrition Aig\xFCe Globale chronique, avec des seuils fix\xE9\
    s selon les normes et la gamme de valeurs class\xE9s de l'OMS."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/78f1816d46af47e99c602f56c060d407/data
  format: null
  id: resource_c15df006
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Prevalence of Global Acute Malnutrition, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/98653f4b88e848d9983efdeee9d9910d/data
  format: PNG
  id: resource_82ed8cb7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e75389fc1cde407bac566e041c8266c1/data
  format: PNG
  id: resource_1448dc66
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Estimated Numbers of Food Insecure People for Long-Term
    Planning
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the estimated population figures\
    \ - by first-level administrative area - estimated for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Burkina Faso in 2018. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: WFP Burkina Faso CO, 2018. Cette couche contient informations\
    \ regard la distribution de la population - par unit\xE9 administrative de deuxi\xE8\
    me niveau - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la\
    \ collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et\
    \ la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es: PAM Bureau du Pays, 2018."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ef7ddf2c7ee34363a6e162d9b6b8b2dd/data
  format: null
  id: resource_9b74f564
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Total Population, 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/54f0e62916b3460492d2f642c1e5b9fb/data
  format: PNG
  id: resource_c1c1ab3d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Areas & Prevalence of Chronic Malnutrition
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e57d014e22cc4dc78d74f7e1c083b89f/data
  format: PNG
  id: resource_ea931810
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Recurrence of Food Insecurity, 2014-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/99fd0eb787f84e0cb6f99635b54711f2/data
  format: PNG
  id: resource_c91b7375
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Areas & Prevalence of Global Acute Malnutrition
    (2013-2017)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6c645fe2ab3345049027c0c5d553d138/data
  format: PNG
  id: resource_15b0ab14
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/588c6b225fd443bb8932078d18ea64ae/data
  format: PNG
  id: resource_d4da4510
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/602b6e2e79dd475d80b393fca1d93e04/data
  format: PNG
  id: resource_1ba54ef8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Estimated Numbers of Additional Food Insecure People
    in case of a Major Shock, 2014-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8ca1b0c2a9744da0b769f8b7246cb136/data
  format: PNG
  id: resource_e8983763
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Most Predominant Livelihood Zones, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f5182aac99b24faf92065380971f27df/data
  format: PNG
  id: resource_6343d717
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a3805aa41a924a739e795ba6075ddf10/data
  format: PNG
  id: resource_6577f0d6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Population Estimates, 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Burkina Faso in\
    \ 2018. The analysis, using the Ministry of Agriculture and Food Security (MASA),\
    \ EPA and Emergency Food Security Assessment (EFSA) data from 2014 to 2018, determines\
    \ the recurrence of food insecurity conditions - by second-level administrative\
    \ area - applying a threshold equal to 15%. Ce document Excel contient l'analyse\
    \ sur l'insecurit\xE9 alimentaire utilis\xE9e aux fins de l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en Burkina Faso en 2018. L'analyse, en utilisant\
    \ Ministry of Agriculture and Food Security (MASA), EPA and Emergency Food Security\
    \ Assessment (EFSA) donn\xE9es du 2014 au 2018, d\xE9termine la r\xE9currence\
    \ de conditions d'insecurit\xE9 alimentaire - par unit\xE9 administrative de premi\xE8\
    re niveau. Le seuil de s\xE9curit\xE9 alimentaire (mesur\xE9 par le score de consommation\
    \ alimentaire pauvre et limite) est fix\xE9 \xE0 15%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dbae3cde9f0a46ecaa513a00d99ad9fb/data
  format: null
  id: resource_f49f2ea0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dceea395131d42cc883f6e62cd1d88d4/data
  format: PNG
  id: resource_df397fc6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the most predominant livelihood\
    \ zones - by first-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Burkina Faso in 2018. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Fewsnet, 2009. Cette couche contient informations regard\
    \ les zones de moyens d'existence pr\xE9dominant - par unit\xE9 administrative\
    \ de premi\xE8re niveau - identifi\xE9es pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Fewsnet, 2009."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5a31260ccb4a43eeab5c627493ed0f80/data
  format: null
  id: resource_eff68483
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Most Predominant Livelihood Zones, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Integrated Context Analysis (ICA), 2018 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2176b2ca0e394c1c98b1e240bc263172/data
  format: PNG
  id: resource_5d962204
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Areas & Land Degradation (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Burkina Faso in 2018,\
    \ showing the areas of convergence of high levels of food insecurity recurrence\
    \ and major propensity to natural shocks (floods and droughts). The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and HQ GIS unit and\
    \ Programme division. Cette couche contient informations regard la classification\
    \ finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en\
    \ Burkina Faso en 2018, montrant les zones de convergence de niveaux elev\xE9\
    s de r\xE9currence d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels\
    \ (inondations et s\xE8cheresse). L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/deda8d6d0aac4579b3adad9129260d10/data
  format: null
  id: resource_022c9ed3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the numbers of food insecure\
    \ people - by first-level administrative unit - estimated for the purposes of\
    \ the Integrated Context Analysis (ICA) run in Burkina Faso in 2018. The analysis\
    \ was a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS\
    \ Unit and Programme division. Data source: Ministry of Agriculture and Food Security\
    \ (MASA) 2014, EPA 2015-2017, Emergency Food Security Analysis (EFSA) 2018. The\
    \ main indicators used for the analysis were the percentage of food insecure population\
    \ for long-term planning and the additional population figures in case of a major\
    \ shock. Cette couche contient informations regard les nombres de personnes expos\xE9\
    es \xE0 l'ins\xE9curit\xE9 alimentaire - par unit\xE9 administrative de premi\xE8\
    re niveau - employ\xE9es pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la\
    \ collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et\
    \ la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es: Ministry of Agriculture and Food Security (MASA) 2014, EPA 2015-2017, Emergency\
    \ Food Security Analysis (EFSA) 2018. Les indicateurs principaux utilis\xE9s pour\
    \ l'analyse \xE9taient la pourcentage de population expos\xE9e \xE0 l'ins\xE9\
    curit\xE9 alimentaire pour la planification \xE0 long-terme et le nombre de personnes\
    \ suppl\xE9mentaires en cas de choc."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6b633c5e1e6f412f8bd90dcbdf357d69/data
  format: null
  id: resource_06b376b8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Estimated Numbers of Food Insecure People, 2014-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by first-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Burkina Faso in 2018. The analysis is the result of a joint effort between\
    \ the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme division.\
    \ Data sources: UNEP/UNISDR GAR 2013. The main indicators used for the analysis\
    \ were the percentage of district surface at flood risk and the maximum expected\
    \ frequency of flood events with a 100-year return period. Cette couche contient\
    \ informations regard le risque d'inondations - par unit\xE9 administrative de\
    \ premi\xE8re niveau - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es : UNEP/UNISDR GAR, 2013. Les indicateurs principaux utilis\xE9es\
    \ pour l'analyse \xE9taient la pourcentage de surface a risuqe d'inondation et\
    \ l'attente maximale attendue des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/61858cb35ce44490aad36bede81e0dd1/data
  format: null
  id: resource_e764c6f9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock risk (floods\
    \ and droughts) estimated during the Integrated Context Analysis (ICA) performed\
    \ in Burkina Faso in 2018. The analysis was a joint effort between the Regional\
    \ Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data sources:\
    \ UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE) 1981-2015.\
    \ Cette couche contient informations regard le risque des chocs naturels (inondations\
    \ et s\xE8cheresse) estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Burkina Faso en 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des donn\xE9es CHIRPS d'estimation\
    \ des precipitations 1981-2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/af68270d17654e9dbae69bdb6e449dec/data
  format: null
  id: resource_c5e11722
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Burkina Faso, 2018 - Natural Shock Risk
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bfa_wfp_integratedcontextanalysis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Burkina Faso: Integrated Context Analysis (ICA), 2018'
version: null
vulnerability: null
---
