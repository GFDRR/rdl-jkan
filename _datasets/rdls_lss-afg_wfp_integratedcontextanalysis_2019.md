---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_afg_2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_afg_2019
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_afg_2019
dataset_id: rdls_lss-afg_wfp_integratedcontextanalysis_2019
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_afg_2019]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend data (2007-2018) with
    natural shock hazard layers (drought, flood, landslide, land degradation) derived
    from observational and satellite data to produce sub-national risk assessments.
    Food insecurity recurrence and severity are mapped against hazard exposure to
    identify areas where different programme interventions (safety nets vs. shock
    recovery) are appropriate.
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
- href: https://data.humdata.org/dataset/wfp_ica_afg_2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought hazard recurrence 2007-2018
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Additional food insecure population vulnerable to shock impacts from
      drought
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
          quantity_kind: currency
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: 'This layer contains information about the recurrence of total food
    insecurity estimated during the Integrated Context Analysis (ICA) run in Afghanistan
    in 2019. Data source: National Risk and Vulnerability Assessment (NRVA) 2007/08,
    Afghanistan Living Condition Survey (ALCS) 2011/12, 2014 and 2017/18. To assess
    the food security trend, the threshold was set to 30% because very close to the
    national average according to the four assessments considered. The key indicator
    used for the analysis was the recurrence of food insecurity above the threshold.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/35f216da275c4558abae45345ebab201/data
  format: null
  id: resource_27162523
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Recurrence of Total Food Insecurity, 2007-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought hazard estimated
    during the Integrated Context Analysis (ICA) performed in Afghanistan in 2019.
    Data source: HQ VAM Analysis of NDVI, NASA Terra MODIS 2013-2018. The key indicator
    used for the purposes of the analysis was the average number of poor growing seasons
    observed in the time frame of interest - by definition, in the context of this
    specific analysis, it is considered a poor growing season when the NDVI observed
    in the single year is significantly below (less than 85%) the long-term average,
    calculated over the last 18 years.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cee984423a8643c0a7db17b2f932885c/data
  format: null
  id: resource_da4d7afc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Drought hazard, 2013-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6c7cecf31ba94be1b700168ad57a3aeb/data
  format: PNG
  id: resource_c33137cf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - Food Insecurity Recurrence
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification deriving
    from the Integrated Context Analysis (ICA) run in Afghanistan in 2019, showing
    the areas of convergence between recurrence of total food insecurity and propensity
    to natural shocks (floods, landslides and drought).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a7edb83b3ee64fb292ed055cb6aadb0a/data
  format: null
  id: resource_b05f8612
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ba5db82604d34036806a8c8c1c5fbd30/data
  format: PNG
  id: resource_0f0ff092
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 Landslide Hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the severity of natural hazards
    (floods, drought and landslides) estimated during the Integrated Context Analysis
    (ICA) performed in Afghanistan in 2019. Data sources: GHM 2009, UNEP/UNISDR GAR
    2013, HQ VAM Analysis of NDVI, NASA Terra MODIS 2013-2018.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0a2e34272d794d97b0e0c4d7386f34e7/data
  format: null
  id: resource_870305f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Natural shock hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the number of food insecure
    people calculated out of the food security assessments used in the Integrated
    Context Analysis (ICA) run in Afghanistan in 2019. Data sources: The key indicators
    used for the purposes of the analysis were the percentage of food insecure people
    for long-term planning and the numbers of additional food insecure people in case
    of a major shock.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1e22ce4f536549cbb6166b63f2f71f86/data
  format: null
  id: resource_84dc0ce8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Estimates of Food Insecure People, 2007-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a336bbda5f0440f9bf954f2c1a8b5d05/data
  format: PNG
  id: resource_541f9a31
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - Food Insecurity Longterm Planning
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ebd45d5845234e9f916fc60759807929/data
  format: PNG
  id: resource_f2839480
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in the Afghanistan in 2019. The analysis brings together the exposure
    of natural shocks (floods, drought and landslides) and the recurrence of food
    insecurity with other key contextual information to provide broad programmatic
    strategies by second-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d63db326b7ba48c38f62144c0264d676/data
  format: null
  id: resource_d04d6420
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f4c9e27e0d4e4db99f2cfc5071f8a6e7/data
  format: PNG
  id: resource_9e9d18fc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Natural Shocks
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the landslide hazard estimated
    during the Integrated Context Analysis (ICA) run in Afghanistan in 2019. Data
    source: UNEP/UNISDR Global Assessment of Risk (GAR), 2013. The key indicators
    used for the analysis were the percentage of surface area affected by landslide
    risk and the maximum expected frequency of landslide events.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d6a535332dd442a7acc7e2d533f3b0e1/data
  format: null
  id: resource_1800883f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Landslide hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/73e5d613294b44c1b83c8d25dd9d27d7/data
  format: PNG
  id: resource_bac27fa5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Drought Hazard 2013-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the Integrated
    Context Analysis (ICA) run in Afghanistan in 2019. Data sources: HQ OSE GIS Analysis
    of NASA MODIS 2001-2016, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
    Model data. The main indicators used for the analysis were the average ecological
    changes observed between 2001-2006 and 2011-2016 and the percentage of erosion-prone
    surface.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/be82de01a62a47e5b00d42faf64131f9/data
  format: null
  id: resource_bb912f61
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Land Degradation, 2001-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2b8335836a5046b8a37a8f040ed6689f/data
  format: PNG
  id: resource_5c7833cb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - Severe and Most Severe Food Insecure Population 2008-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/65d0dd5c4c744e0fa0ee1eb285676706/data
  format: PNG
  id: resource_58331517
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Flood Hazard 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/39c75ecdbff2455d930483ff7ea0db6b/data
  format: PNG
  id: resource_7e12c7cf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - Additional Food Insecure Population in case of Shock
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Integrated Context Analysis (ICA), 2019 (No abstract
    provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/41f12989e442435c8f356849d6fd97dd/data
  format: PNG
  id: resource_2ad789c0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan 2019 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition levels observed
    during the Integrated Context Analysis (ICA) run in Afghanistan in 2019. Data
    source: Afghanistan Health Survey (AHS), 2018. The key indicator used for the
    purposes of the analysis was the prevalence of Global Acute Malnutrition (GAM)
    in children below 5 years of age.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3a095d32d7c548fbaaab18b0da20e3dc/data
  format: null
  id: resource_bbf5cd69
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Prevalence of Global Acute Malnutrition (GAM), 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of severe and
    very severe food insecurity estimated during the Integrated Context Analysis (ICA)
    run in Afghanistan in 2019. Data source: National Risk and Vulnerability Assessment
    (NRVA) 2007/08, Afghanistan Living Condition Survey (ALCS) 2011/12, 2014 and 2017/18.
    To assess the food security trend and considering an average national food insecurity
    close to 30%, the threshold was set to 10% to better identify the most vulnerable
    districts. The key indicator used for the analysis was the recurrence of severe
    and very severe food insecurity above the threshold.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2c5a9dadbfd745a6865687cff10419c6/data
  format: null
  id: resource_d169c955
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Recurrence of Severe and Very Severe Food Insecurity,
    2007-2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Excel file contains the food insecurity analysis performed for
    the purposes of the Integrated Context Analysis (ICA) run in Afghanistan in 2019.
    The analysis, using NRVA and ALCS data from 2007/08 to 2017/18, determines the
    recurrence of total food insecurity conditions - by second-level administrative
    area - applying a threshold equal to 30%.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f62b173acae04345a623ea128312f6e1/data
  format: null
  id: resource_f9621dcf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Afghanistan, 2019 - Total Food Insecurity Recurrence Analysis
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_wfp_integratedcontextanalysis_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: 'Afghanistan: Integrated Context Analysis (ICA), 2019'
version: null
vulnerability: null
---
