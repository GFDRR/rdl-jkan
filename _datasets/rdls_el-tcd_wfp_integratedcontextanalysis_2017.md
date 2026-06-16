---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_tcd_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tcd_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tcd_2017
dataset_id: rdls_el-tcd_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_tcd_2017]'
details: null
exposure:
- asset_type:
    description: Human settlements and population distribution across Chad
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
    description: Agricultural land and food security-dependent populations
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
  description: The ICA combines multi-year food security trend data with natural shock
    risk assessments (drought, flood, landslide, land degradation) to produce sub-national
    risk maps. Hazard data derives from historical observations (1981-2015 for drought,
    2001-2012 for land degradation, 2013 for rapid-onset shocks) and are integrated
    with population and agricultural exposure data to estimate food insecurity impacts
    and identify areas requiring different programme strategies.
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
- href: https://data.humdata.org/dataset/wfp_ica_tcd_2017
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence and additional food insecure populations
      from drought shocks
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
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity impacts from rapid-onset flood shocks
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity impacts from landslide hazards
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
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a95b50b9f5a34334ae197127bf180d65/data
  format: PNG
  id: resource_6fb1e859
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Areas & Prevalence of Global Acute Malnutrition, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by second-level administrative area - observed for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Chad in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data sources: HQ OSEP GIS Analysis of NASA MODIS 2001-2012, WorldClim\
    \ 1970-2000, FAO data and NASA SRTM Digital Elevation Model. The main indicators\
    \ used for the analysis were the average ecological changes observed between 2001\
    \ and 2012 and the percentage of erosion-prone surface. Cette couche contient\
    \ les donn\xE9es necessaires pour determiner le niveau de d\xE9gradation des terres\
    \ - par unit\xE9 administrative de deuxi\xE8me niveau - observ\xE9 pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en 2017. L'analyse a \xE9\
    t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de\
    \ Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier g\xE9n\xE9\
    rale du PAM. Source des donn\xE9es: HQ OSEP GIS Analyse des donn\xE9es NASA MODIS\
    \ 2001-2012, WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation Model. Les\
    \ indicateurs principaux utilis\xE9s pour l'analyse \xE9taient les changements\
    \ moyens de couverture du sol observ\xE9s entre 2001 et 2012 et la pourcentage\
    \ de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f2e8666ffe33458e87c875dbcc9e7e66/data
  format: null
  id: resource_98f8bb85
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Chad in 2017. The\
    \ analysis, using the Enqu\xEAte Nationale de la S\xE9curit\xE9 (ENSA) data from\
    \ 2011 to 2016, determines the recurrence of food insecurity conditions - by second-level\
    \ administrative area - applying a threshold equal to 20%. Ce document Excel contient\
    \ l'analyse sur l'insecurit\xE9 alimentaire utilis\xE9e aux fins de l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en 2017. L'analyse, en utilisant\
    \ les 'Enqu\xEAte Nationale de la S\xE9curit\xE9' (ENSA) donn\xE9es du 2011 au\
    \ 2016, d\xE9termine la r\xE9currence de conditions d'insecurit\xE9 alimentaire\
    \ - par unit\xE9 administrative de deuxi\xE8me niveau. Le seuil de s\xE9curit\xE9\
    \ alimentaire (mesur\xE9 par le score de consommation alimentaire pauvre et limite)\
    \ est fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7416c4868bb14516a5ac0d8ed1d7165d/data
  format: null
  id: resource_4292e3d4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Food Security Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the main human settlements ,\
    \ codified by the ICA Categories of the relative department, used in the Integrated\
    \ Context Analysis (ICA) run in Chad in 2017. Cette couche contient information\
    \ regard les principaux \xE9tablissements humains, codifi\xE9s selon les Cat\xE9\
    gories ICA du d\xE9partement relatif, utilis\xE9s pour l'Analyse Integr\xE9e du\
    \ Contexte (AIC) execut\xE9e en Tchad en 2017."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bfe34e3128bf4d95bc69115e8f0176bd/data
  format: null
  id: resource_772b15bb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA-Coded Human Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Chad in 2017. The analysis is a joint effort between the Regional Bureau\
    \ in Dakar (RBD), the HQ GIS Unit and Programme division. Data source: HQ VAM\
    \ Analysis of Chirps Rainfall Estimates (RFE), 1981-2015. The main indicator used\
    \ for the analysis was the number of poor growing seasons observed in the time\
    \ window of interest. Cette couche contient informations regard le risque de s\xE8\
    cheresse - par unit\xE9 administrative de deuxi\xE8me niveau - estim\xE9e pendant\
    \ l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en 2017. L'analyse\
    \ a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9\
    gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier\
    \ g\xE9n\xE9rale du PAM. Source des donn\xE9es: HQ VAM Analyse des donn\xE9es\
    \ CHIRPS d'estimation des precipitations, 1981-2015. L'indicateur principale utilis\xE9\
    \ pour l'analyse \xE9tait le nombre de saisons qui ont connu un d\xE9ficit hydrique\
    \ (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dd3e1265876d4ac5a82393ab4f9ec7f1/data
  format: null
  id: resource_b6945f86
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c9dada918c40461d813701a0b5b82b9d/data
  format: PNG
  id: resource_46279774
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Rapid On-Set Shock Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the landslide hazard estimated\
    \ - by second-level administrative area - during the Integrated Context Analysis\
    \ (ICA) run in Chad in 2017. Data source: UNEP/UNISDR GAR 2013. The main indicators\
    \ used for the analysis were the percentage of department surface at landslide\
    \ hazard, the maximum expected frequency of landslide events. Cette couche contient\
    \ informations regard le risque des glissements de terraine - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - estim\xE9 pendant l'Analyse Integr\xE9e de Contexte\
    \ (AIC) ex\xE9cut\xE9 en Tchad en 2017. Sources des donn\xE9es: UNEP/UNISDR GAR\
    \ 2013. Les indicateurs principales utilis\xE9s pour l'analyse \xE9taient la pourcentage\
    \ de surface \xE0 risque des glissements de terraine et l'attente maximale attendue\
    \ des glissements de terraine."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bcd39d1f84a54d4281be59c616ca8d4f/data
  format: null
  id: resource_140e7c17
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Landslide Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Chad in 2017. The analysis brings together the historical\
    \ risk of natural shocks (floods, droughts and landslides) and the recurrence\
    \ of high food insecurity with other key contextual information to provide broad\
    \ programmatic strategies by second-level administrative area. Ce document contient\
    \ les r\xE9sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Tchad en 2017. L'analyse rassemble le risque historique des chocs naturels\
    \ (inondations, s\xE8cheresse et glissements de terrain) et la r\xE9currence elev\xE9\
    e d'ins\xE9curit\xE9 alimentaire avec autres informations contextuelles afin de\
    \ fournir grandes strat\xE9gies programmatiques par unit\xE9 administrative de\
    \ deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/eb977abdba644f3db8728f9963f43c1f/data
  format: null
  id: resource_2986e3d1
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Chad in 2017, showing\
    \ the areas of convergence of high levels of food insecurity recurrence and major\
    \ propensity to natural shocks (floods, droughts and landslides). The analysis\
    \ was a joint effort between the Regional Bureau in Dakar (RBD) and HQ GIS unit\
    \ and Programme division. Cette couche contient informations regard la classification\
    \ finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en\
    \ Tchad en 2017, montrant les zones de convergence de niveaux elev\xE9s de r\xE9\
    currence d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels (inondations,\
    \ s\xE8cheresse et glissements de terrain). L'analyse a \xE9t\xE9 execut\xE9e\
    \ gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f1919d25e3b24e5aa0ad9e60f165a44c/data
  format: null
  id: resource_5fbf6078
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Chad in 2017. The analysis brings together the historical\
    \ risk of natural shocks (floods, droughts and landslides) and the recurrence\
    \ of high food insecurity with other key contextual information to provide broad\
    \ programmatic strategies by second-level administrative area. Ce document contient\
    \ les r\xE9sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Tchad en 2017. L'analyse rassemble le risque historique des chocs naturels\
    \ (inondations, s\xE8cheresse et glissements de terrain) et la r\xE9currence elev\xE9\
    e d'ins\xE9curit\xE9 alimentaire avec autres informations contextuelles afin de\
    \ fournir grandes strat\xE9gies programmatiques par unit\xE9 administrative de\
    \ deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/097ae591a6004188acc8632211983894/data
  format: null
  id: resource_b4bd26a9
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Programmatic Recommendations Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/20b07a624bb04b9199c33a849333e747/data
  format: PNG
  id: resource_3c18fed2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fbff1424ade54ec8b0796eb2c4c6d480/data
  format: PNG
  id: resource_43f0920f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Recurrence of Food Insecurity
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock risk (floods\
    \ and droughts) estimated during the Integrated Context Analysis (ICA) performed\
    \ in Chad in 2017. The analysis was a joint effort between the Regional Bureau\
    \ in Dakar (RBD), the HQ GIS Unit and Programme division. Data sources: UNEP/UNISDR\
    \ GAR 2013, HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE) 1981-2015. Cette\
    \ couche contient informations regard le risque des chocs naturels (inondations\
    \ et s\xE8cheresse) estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Tchad en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des donn\xE9es CHIRPS d'estimation des\
    \ precipitations 1981-2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/60d3191f0aa8432c8f66b7ce437f91c6/data
  format: null
  id: resource_2c48e7fe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/25cadee821af4272963a428e8ec520c4/data
  format: PNG
  id: resource_901412e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Categories & Land Degradation (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ac29b0ebfcf14fd29eb0746fe6517732/data
  format: PNG
  id: resource_42fd5b51
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Landslide Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5336aeaac80d4498a20509a1093baadd/data
  format: PNG
  id: resource_c6301f71
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Number of Additional Food Insecure People in case of a Major
    Shock, 2011-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/36ff611ca04641a18d7bac44840f829b/data
  format: PNG
  id: resource_00b2840d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0fa686dd3e9c49b1af4ec8ed3f63a31a/data
  format: PNG
  id: resource_8adc0248
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8e2deb54bc4149c8952494ab529daf9d/data
  format: PNG
  id: resource_0869aa8e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the rapid on-set shocks risk\
    \ (floods and landslides) - by second-level administrative unit - estimated during\
    \ the Integrated Context Analysis (ICA) run in Niger in 2017. Data source: UNEP/UNISDR\
    \ GAR 2013. Cette couche contient informations regard le risque de chocs de d\xE9\
    clanchement rapide (inondations et glissements de terrain) - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - estim\xE9 pendant l'Analyse Integr\xE9e de Contexte\
    \ (AIC) execut\xE9 en Tchad en 2017. Source des donn\xE9es: UNEP/UNISDR GAR 2013."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4105eb8a516d47e2a92965a7c01cb517/data
  format: null
  id: resource_302d8d9e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Rapid On-Set Shock Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/738c05c76f7e4bd0ac3c6aafd3dff081/data
  format: PNG
  id: resource_4bb14cfe
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Percentage of Food Insecure People for Long-Term Planning,
    2011-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e1932950c3bb49fb9b75c879c8e55cba/data
  format: PNG
  id: resource_5c2680af
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/94c1a95a91c041dda965ddcaf8ff13d9/data
  format: PNG
  id: resource_02c495bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Most Predominant Livelihood Zones (2011) & ICA-Coded Human
    Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/66d2b54d27d84047a8a72552933504df/data
  format: PNG
  id: resource_b6462f8a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the numbers of food insecure\
    \ people - by second-level administrative unit - estimated for the purposes of\
    \ the Integrated Context Analysis (ICA) run in Chad in 2017. The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit\
    \ and Programme division. Data source: Enqu\xEAte Nationale de la S\xE9curit\xE9\
    \ Alimentaire et Nutritionnelle (ENSA), 2011-2016. The main indicators used for\
    \ the analysis were the percentage of food insecure population for long-term planning\
    \ and the additional population figures in case of a major shock. Cette couche\
    \ contient informations regard les nombres de personnes expos\xE9es \xE0 l'ins\xE9\
    curit\xE9 alimentaire - par unit\xE9 administrative de deuxi\xE8me niveau - employ\xE9\
    es pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en 2017.\
    \ L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau\
    \ R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier\
    \ g\xE9n\xE9rale du PAM. Source des donn\xE9es: Enqu\xEAte Nationale de la S\xE9\
    curit\xE9 Alimentaire et Nutritionnelle (ENSA), 2011-2016. Les indicateurs principaux\
    \ utilis\xE9s pour l'analyse \xE9taient la pourcentage de population expos\xE9\
    e \xE0 l'ins\xE9curit\xE9 alimentaire pour la planification \xE0 long-terme et\
    \ le nombre de personnes suppl\xE9mentaires en cas de choc."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a2155e79a5484792b03dbbfa3a9879ea/data
  format: null
  id: resource_8357ebeb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Estimates of Food Insecure People, 2011-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Chad in 2017. The analysis is the result of a joint effort between the\
    \ Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme division. Data\
    \ sources: UNEP/UNISDR GAR 2013. The main indicators used for the analysis were\
    \ the percentage of department surface at flood risk and the maximum expected\
    \ frequency of flood events with a 100-year return period. Cette couche contient\
    \ informations regard le risque d'inondations - par unit\xE9 administrative de\
    \ deuxi\xE8me niveau - estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Tchad en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es : UNEP/UNISDR GAR, 2013. Les indicateurs principaux utilis\xE9es pour l'analyse\
    \ \xE9taient la pourcentage de surface a risque d'inondation et l'attente maximale\
    \ attendue des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/427f852863904dfda9f50d79d919d65e/data
  format: null
  id: resource_35afbdf7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food security trend analysis\
    \ - by second-level administrative unit - used for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Chad in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Enqu\xEAte Nationale de la S\xE9curit\xE9 (ENSA), 2011-2016.\
    \ The main indicator used for the analysis was the Food Consumption Score (FCS),\
    \ with a threshold - referring to poor and borderline households - set to 20%.\
    \ Cette couche contient les donn\xE9es d'une analyse de tendance de la s\xE9curit\xE9\
    \ alimentaire - par unit\xE9 administrative de deuxi\xE8me niveau - employ\xE9\
    e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en 2017.\
    \ L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau\
    \ R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier\
    \ g\xE9n\xE9rale du PAM. Source des donn\xE9es: Enqu\xEAte Nationale de la S\xE9\
    curit\xE9 (ENSA), 2011-2016 L'indicateur principale utilis\xE9 pour l'analyse\
    \ \xE9tait le score de consommation alimentaire faible et limite, avec un seuil\
    \ fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f2d441a884834943ad8eb9a8ec83f143/data
  format: null
  id: resource_7e0c66cf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Recurrence of Food Insecurity, 2011-2016
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-tcd_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Chad: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---
