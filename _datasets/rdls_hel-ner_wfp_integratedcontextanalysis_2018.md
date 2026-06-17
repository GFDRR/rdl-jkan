---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme (WFP)
    url: https://data.humdata.org/dataset/wfp_ica_ner_2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWS NET Livelihood Zones, 2011
    url: https://data.humdata.org/dataset/wfp_ica_ner_2018
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_ner_2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_ner_2018
dataset_id: rdls_hel-ner_wfp_integratedcontextanalysis_2018
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_ner_2018]'
details: null
exposure:
- asset_type:
    description: Population density data (2015) used to characterize exposure of people
      to natural shocks and food insecurity in Niger
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
    description: Livelihood zones (2011) representing agricultural and pastoral land
      use systems across Niger
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend data (2013-2017) with
    natural shock risk layers (flood risk 2013, drought risk 1981-2015) and exposure
    data (population density, livelihood zones, land degradation) through a spatial
    overlay and consultation process. Sub-national administrative units are classified
    into ICA categories reflecting combinations of chronic food insecurity and shock
    risk to guide programmatic targeting. The resulting maps and analysis support
    WFP strategic planning for food security and resilience programming in Niger.
  sources:
  - id: source_1
    license: null
    name: World Food Programme (WFP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: FEWS NET Livelihood Zones, 2011
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_ner_2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of additional food insecure people in case of a
      major flood shock, 2013-2017
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
    description: Estimated number of additional food insecure people in case of a
      major drought shock, based on recurrence analysis 2013-2017
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: AA:km2
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
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Niger between 2017 and\
    \ 2018, showing the areas of convergence of high levels of food insecurity recurrence\
    \ and major propensity to natural shocks (floods and droughts). The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and HQ GIS unit and\
    \ Programme division. Cette couche contient informations regard la classification\
    \ finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en\
    \ Niger entre 2017 et 2018, montrant les zones de convergence de niveaux elev\xE9\
    s de r\xE9currence d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels\
    \ (inondations et s\xE8cheresse). L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/04d1e9cca2884ac0baa2d6a45516f18e/data
  format: null
  id: resource_f347ee15
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Niger between 2017 and 2018. The analysis is the result of a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data sources: UNEP/UNISDR GAR 2013. The main indicators used for the\
    \ analysis were the percentage of district surface at flood risk and the maximum\
    \ expected frequency of flood events with a 100-year return period. Cette couche\
    \ contient informations regard le risque d'inondations - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - estim\xE9 pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Niger entre 2017 et 2018. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es : UNEP/UNISDR GAR, 2013. Les indicateurs principaux utilis\xE9es\
    \ pour l'analyse \xE9taient la pourcentage de surface a risuqe d'inondation et\
    \ l'attente maximale attendue des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/87be938d587342edbd19434ca716be80/data
  format: null
  id: resource_3467100e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock risk (floods\
    \ and droughts) estimated during the Integrated Context Analysis (ICA) performed\
    \ in Niger between 2017 and 2018. The analysis was a joint effort between the\
    \ Regional Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data\
    \ sources: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS Rainfall Estimates\
    \ (RFE) 1981-2015. Cette couche contient informations regard le risque des chocs\
    \ naturels (inondations et s\xE8cheresse) estim\xE9 pendant l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en Niger entre 2017 et 2018. L'analyse a \xE9\
    t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de\
    \ Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier g\xE9n\xE9\
    rale du PAM. Source des donn\xE9es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des\
    \ donn\xE9es CHIRPS d'estimation des precipitations 1981-2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/70a7636e1a484046acf0007bbc241e21/data
  format: null
  id: resource_eaecfe22
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the most predominant livelihood\
    \ zones - by second-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Niger between 2017 and 2018. The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit\
    \ and Programme division. Data source: Fewsnet, 2011. Cette couche contient informations\
    \ regard les zones de moyens d'existence pr\xE9dominant - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - identifi\xE9es pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Niger entre 2017 et 2018. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Fewsnet, 2011."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d8195c08a6404fae9bd8c4a6dee7b7bc/data
  format: null
  id: resource_9f7b02b0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Most Predominant Livelihood Zones, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b1766d70ae0a4ffb82d960aeefaac9e1/data
  format: PNG
  id: resource_964ec790
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dc95b6b8fd1d4ab6b958313c30cf9bcf/data
  format: PNG
  id: resource_0ac16a67
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bfbea2030b0441e6854bf58c2088f50f/data
  format: PNG
  id: resource_9876748f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Recurrence of Food Insecurity, 2013-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9c84e2569f2e45fab0b0e522b2adc111/data
  format: PNG
  id: resource_a6bfc55e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/386d6b1e7ce34a11bb7cf85705add4d1/data
  format: PNG
  id: resource_01f6f6e3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Areas & Land Degradation (2001-2013)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/13b047120715445b972381a848e0837d/data
  format: PNG
  id: resource_4e316199
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Areas & Prevalence of Global Acute Malnutrition, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c8b6569552d84cfe8b97c1f0ed202ff9/data
  format: PNG
  id: resource_55b1c71d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Most Predominant Livelihood Zones, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dc28f8f88be048838b998819ffa327db/data
  format: PNG
  id: resource_5da8b31f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Niger between 2017 and 2018. The analysis brings together\
    \ the historical risk of natural shocks (floods and droughts) and the recurrence\
    \ of high food insecurity with other key contextual information to provide broad\
    \ programmatic strategies by second-level administrative area. Ce document contient\
    \ les r\xE9sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Niger entre 2017 et 2018. L'analyse rassemble le risque historique des chocs\
    \ naturels (inondations et s\xE8cheresse) et la r\xE9currence elev\xE9e d'ins\xE9\
    curit\xE9 alimentaire avec autres informations contextuelles afin de fournir grandes\
    \ strat\xE9gies programmatiques par unit\xE9 administrative de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d9d06a563cf04e2eb5a6bac64de9aaac/data
  format: null
  id: resource_1c6f45ce
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/802e794c556f442d8168cf375957424f/data
  format: PNG
  id: resource_12d0ae7c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Estimated Number of Additional Food Insecure People in
    case of a Major Shock, 2013-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ee574a1dcb1a45f5a0018454dbe9f5c4/data
  format: PNG
  id: resource_e2ce91d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the malnutrition levels - by\
    \ first-level administrative unit - used for the purposes of the Integrated Context\
    \ Analysis (ICA) run in Niger between 2017 and 2018. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and HQ GIS Unit and Programme\
    \ division. Data source: Standardized Monitoring and Assessment of Relief and\
    \ Transitions (SMART), 2016. The main indicator used for the analysis was the\
    \ prevalence of Global Acute Malnutrition (GAM), with a threshold set to 10% according\
    \ to the guidelines suggested by the World Health Organization (WHO). Cette couche\
    \ contient informations regard les niveaux de malnutrition - par unit\xE9 administrative\
    \ de premi\xE8re niveau - observ\xE9s pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Niger entre 2017 et 2018. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait la pr\xE9valence de Malnutrition\
    \ Aig\xFCe Globale (MAG), avec un seuil d'alerte fix\xE9 \xE0 10%, selon les normes\
    \ et la gamme de valeurs class\xE9s de l'OMS 2006."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5881c9743f344864947cf2482c077e02/data
  format: null
  id: resource_c8846d17
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Prevalence of Global Acute Malnutrition, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Niger between 2017 and 2018. The analysis is a joint effort between the\
    \ Regional Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data\
    \ source: HQ VAM Analysis of Chirps Rainfall Estimates (RFE), 1981-2015. The main\
    \ indicator used for the analysis was the number of poor growing seasons observed\
    \ in the time window of interest. Cette couche contient informations regard le\
    \ risque de s\xE8cheresse - par unit\xE9 administrative de deuxi\xE8me niveau\
    \ - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en\
    \ Niger entre 2017 et 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la\
    \ collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et\
    \ la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es: HQ VAM Analyse des donn\xE9es CHIRPS d'estimation des precipitations, 1981-2015.\
    \ L'indicateur principale utilis\xE9 pour l'analyse \xE9tait le nombre de saisons\
    \ qui ont connu un d\xE9ficit hydrique (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/19515ea866434d1092cae545211a3805/data
  format: null
  id: resource_62f88ddf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by second-level administrative area - observed for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Niger between 2017 and 2018. The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit\
    \ and Programme division. Data sources: HQ OSEP GIS Analysis of NASA MODIS 2001-2013,\
    \ WorldClim 1970-2000, FAO data and NASA SRTM Digital Elevation Model. The main\
    \ indicators used for the analysis were the average ecological changes observed\
    \ between 2001 and 2012 and the percentage of erosion-prone surface. Cette couche\
    \ contient les donn\xE9es necessaires pour determiner le niveau de d\xE9gradation\
    \ des terres - par unit\xE9 administrative de deuxi\xE8me niveau - observ\xE9\
    \ pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Niger entre 2017\
    \ et 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre\
    \ le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme\
    \ au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: HQ OSEP GIS Analyse\
    \ des donn\xE9es NASA MODIS 2001-2013, WorldClim 1970-2000, FAO et NASA SRTM Digital\
    \ Elevation Model. Les indicateurs principaux utilis\xE9s pour l'analyse \xE9\
    taient les changements moyens de couverture du sol observ\xE9s entre 2001 et 2012\
    \ et la pourcentage de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5ffdc36cb43942c2afc2f6ec2abbe9ae/data
  format: null
  id: resource_8e805f32
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Land Degradation, 2001-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger: Integrated Context Analysis (ICA), 2018 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/39a6a7cfcfc44511a122721eaec72097/data
  format: PNG
  id: resource_8a19186b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Niger between 2017\
    \ and 2018. The analysis, using the Food Security Monitoring System (FSMS) data\
    \ from 2013 to 2017, determines the recurrence of food insecurity conditions -\
    \ by second-level administrative area - applying a threshold equal to 20%. Ce\
    \ document Excel contient l'analyse sur l'insecurit\xE9 alimentaire utilis\xE9\
    e aux fins de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Niger entre\
    \ 2017 et 2018. L'analyse, en utilisant Food Security Monitoring System (FSMS)\
    \ donn\xE9es du 2013 au 2017, d\xE9termine la r\xE9currence de conditions d'insecurit\xE9\
    \ alimentaire - par unit\xE9 administrative de deuxi\xE8me niveau. Le seuil de\
    \ s\xE9curit\xE9 alimentaire (mesur\xE9 par le score de consommation alimentaire\
    \ pauvre et limite) est fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/68aaf50f834f473a93b24f04aba2bc52/data
  format: null
  id: resource_4e9abbd5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Food Security Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food security trend analysis\
    \ - by second-level administrative unit - used for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Niger between 2017 and 2018. The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit\
    \ and Programme division. Data source: Food Security Monitoring System (FSMS),\
    \ 2013-2017. The main indicator used for the analysis was the Food Consumption\
    \ Score (FCS), with a threshold - referring to poor and borderline households\
    \ - set to 20%. Cette couche contient les donn\xE9es d'une analyse de tendance\
    \ de la s\xE9curit\xE9 alimentaire - par unit\xE9 administrative de deuxi\xE8\
    me niveau - employ\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Niger entre 2017 et 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es: Food Security Monitoring System (FSMS), 2013-2017. L'indicateur principale\
    \ utilis\xE9 pour l'analyse \xE9tait le score de consommation alimentaire faible\
    \ et limite, avec un seuil fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d96e246e364141bf8def2696df8a82ed/data
  format: null
  id: resource_129b8e93
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Niger, 2018 - Recurrence of Food Insecurity, 2013-2017
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ner_wfp_integratedcontextanalysis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Niger: Integrated Context Analysis (ICA), 2018'
version: null
vulnerability: null
---
