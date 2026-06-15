---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_tjk_2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tjk_2015
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tjk_2015
dataset_id: rdls_el-tjk_wfp_integratedcontextanalysis_2015
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_tjk_2015]'
details: null
exposure:
- asset_type:
    description: Rural population distribution at sub-national level, 2013
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
    description: Human settlements and settlement locations, 2007
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Land cover and land degradation patterns 2001-2012
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA integrates historical natural shock risk data (flood, mudflow,
    drought 1998-2011) with food security trend analysis (2008-2012) and land degradation/cover
    change mapping (2001-2012) to identify sub-national areas where different programme
    strategies are appropriate for reducing food insecurity and climate-related shock
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
- href: https://data.humdata.org/dataset/wfp_ica_tjk_2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by recurrent food insecurity linked to flood
      shocks 2008-2012
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
    description: Population affected by recurrent food insecurity linked to drought
      shocks 2008-2012
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
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) run in Tajikistan in 2015. Data source:
    Committee of Emergency Situations and Civil Defense (CoES CD), 1998-2011. The
    key indicator used for the analysis was the overall number of flood disasters.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/651e18d7de3c48a79efbda9c82af17b5/data
  format: null
  id: resource_9842ea8d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Flood Risk, 1998-2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the rural population - by district
    level - living in Tajikistan and mapped for the purposes of the Integrated Context
    Analysis (ICA) run in 2015. Data source: WFP CO, 2013.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/083d592eeca24a25bd5abbd13ee67519/data
  format: null
  id: resource_86f900b7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Rural Population, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA) run in Tajikistan in 2015, showing
    the areas of convergence between high levels of food insecurity and high propensity
    to natural shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f69ab648eda248e28d22cb896f2ac80f/data
  format: null
  id: resource_7afa2365
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/807d689fd9da4765bb4e3e0ffcce1fb1/data
  format: PNG
  id: resource_bdc294a3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - High Population Density
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f916a6e442a54724aac909972a522947/data
  format: PNG
  id: resource_7907f6bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the natural shocks risk (floods,
    mudflows and droughts) estimated during the Integrated Context Analysis (ICA)
    run in Tajikistan in 2015. Data source: Committee of Emergency Situations and
    Civil Defense (CoES CD), 1998-2011.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5d4974dfdb874d9caf2983675bc0c200/data
  format: null
  id: resource_ce324b3a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Natural Shocks Risk, 1998-2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the mudflow risk estimated during
    the Integrated Context Analysis (ICA) run in Tajikistan in 2015. Data source:
    Committee of Emergency Situations and Civil Defense (CoES CD), 1998-2011. The
    key indicator used for the analysis was the overall number of mudflow/flash flood
    disasters.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cc4235105b09416ca56fb32f5b91e178/data
  format: null
  id: resource_3a346fd1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Mudflow Risk, 1998-2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the food insecurity level estimated
    during the Integrated Context Analysis (ICA) run in Tajikistan in 2015. Data source:
    WFP FSMS surveys, 2008-2012. The data were originally collected by livelihood
    zone and afterwards proportionally re-attributed to the districts falling within
    or across the zones. The key indicators used for the analysis were the recurrence
    above the 20% threshold - the difference between the average food security value
    for the area and the national average - , the average against national average
    and the variability/stability.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/416cc9f9b81e4d2e96a7a838d389288e/data
  format: null
  id: resource_b97d8224
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Recurrence of Food insecurity, 2008-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7fdd0b655f6d43929cd6e487309ecbe4/data
  format: PNG
  id: resource_6abaefeb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/43e15f2343274553823968e1ea95056b/data
  format: PNG
  id: resource_87a1e91a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Erosion Propensity, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/212181a7ba494cb193d16a24065cdbeb/data
  format: PNG
  id: resource_6f377d6d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Food Insecurity Risk, 2008-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9908ad4290434a56889f812ab9a124c8/data
  format: PNG
  id: resource_660fe83c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/65727b412a614829893e838390b6fa66/data
  format: PNG
  id: resource_05610d77
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Land Degradation & High Population Density
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/782b9b855dcb4cb9a3b6f9e260fc6710/data
  format: PNG
  id: resource_83a98a46
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Land Cover Change, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the geographical position (latitude
    and longitude) of the human settlements used during the Integrated Context Analysis
    (ICA) run in Tajikistan in 2015. Data source: Global Discovery, 2007.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d561e12d372547959ec7a14b44d76ec2/data
  format: null
  id: resource_9858db67
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Human Settlements, 2007
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    estimated during the Integrated Context Analysis (ICA) run in Tajikistan in 2015.
    Data source: NASA MODIS 2001-2012, FAO, NASA SRTM Digital Elevation Model (500m
    resolution). The key indicators used for the analysis were the average land cover
    change observed in the reference time frame and percentage of district area affected
    by erosion.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b68395f620524194af352d7934082f7f/data
  format: null
  id: resource_4e1af2a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) run in Tajikistan in 2015. Data source:
    Committee of Emergency Situations and Civil Defense (CoES CD), 1998-2011. The
    key indicator used for the analysis is the overall number of drought disasters.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5639058dd5b341048a61110d35caca14/data
  format: null
  id: resource_feb9e6af
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Drought Risk, 1998-2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tajikistan: Integrated Context Analysis (ICA), 2015 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/282b29da85ec4d2eb7ef227099686b69/data
  format: PNG
  id: resource_4c19e553
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Predominant Livelihood Zones, Land Degradation & Human
    Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food security analysis performed for the
    purposes of the Integrated Context Analysis (ICA) run in Tajikistan in 2015. The
    analysis, using the Food Security Monitoring System (FSMS) data from 2008 to 2012,
    determines the recurrence of food insecurity conditions - by second-level administrative
    area - applying a threshold equal to 20% using the methodology elaborated by HQ
    OSEP GIS Team and VAM which considers the difference between the average food
    security value for the area and the national average, the average against national
    average and the variability/stability.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/88ecce925b2a4c53acd288b5f716f876/data
  format: null
  id: resource_07a5262c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the predominant livelihood zones
    - by district level - elaborated during the Integrated Context Analysis (ICA)
    run in Tajikistan in 2015. Data source: HQ OSEP GIS Analysis of Fewsnet, 2011.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b57c6fcec7ed44cba50eff9729b9ce2c/data
  format: null
  id: resource_c71fa119
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Predominant Livelihood Zones, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the rapid on-set shocks risk
    (floods & mudflows) estimated during the Integrated Context Analysis (ICA) run
    in Tajikistan in 2015. Data source: Committee of Emergency Situations and Civil
    Defense (CoES CD), 1998-2011.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/88ab21ad589e4f86a8a70ae8345802f9/data
  format: null
  id: resource_48931bef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Rapid On-Set Shocks Risk, 1998-2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the 2015 Integrated Context Analysis
    (ICA) conducted in Tajikistan. The analysis brings together the historical risk
    of natural shocks (floods, mudflows and drought) and the recurrence of high food
    insecurity with other key contextual information to provide broad programmatic
    strategies at district-level based on each district profile.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8083223ab9d0420c958c6731501d3fbc/data
  format: null
  id: resource_22fb9bac
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Tajikistan, 2015 - Technical Paper & Programmatic Recommendations
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-tjk_wfp_integratedcontextanalysis_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - TJK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: 'Tajikistan: Integrated Context Analysis (ICA), 2015'
version: null
vulnerability: null
---
