---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_syr_2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_syr_2020
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_syr_2020
dataset_id: rdls_lss-syr_wfp_arabrepublicintegratedcon_2020
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_syr_2020]'
details: null
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trend data (2015-2019) with
    observed natural hazard maps (flood 2013, drought 1982-2019, land degradation
    2001-2016) and nutritional indicators to produce a strategic analysis identifying
    sub-national areas where food insecurity is driven by chronic vulnerability versus
    acute shock exposure. Hazard severity and recurrence data are overlaid with food
    insecurity estimates to classify programme intervention priorities.
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
- href: https://data.humdata.org/dataset/wfp_ica_syr_2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity recurrence linked to flood hazard exposure
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
    description: Food insecurity and malnutrition linked to drought hazard exposure
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
  description: 'This layer contains information about the food security trend analysis
    - by second-level administrative unit - used for the purposes of the update of
    the Integrated Context Analysis (ICA) run in the Syrian Arab Republic in 2020.
    Data source: FSA-FSLA, 2015-2019. The main indicator used for the analysis was
    the CARI (Consolidated Approach to Reporting Indicators of Food Security) indicator,
    with a threshold - referring to moderately and severely food insecure households
    - set to 33%.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f0644af387c843f49354dc29a4a4a9cf/data
  format: null
  id: resource_1673535e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Recurrence of food insecurity, 2015-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood hazard - by second-level
    administrative unit - estimated during the update of the Integrated Context Analysis
    (ICA) run in the Syrian Arab Republic in 2020. Data sources: UNEP/UNISDR GAR 2013.
    The main indicators used for the analysis were the percentage of department surface
    at flood hazard and the maximum expected frequency of flood events with a 100-year
    return period.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0cf6e498f1444e818f108e17b0448b6a/data
  format: null
  id: resource_5e7274d6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Flood hazard, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the severity of natural hazards
    (floods and droughts) - by second-level administrative unit - estimated during
    the update of the Integrated Context Analysis (ICA) performed in the Syrian Arab
    Republic in 2020. Data sources: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS
    Rainfall Estimates (RFE) 1982-2016, SYR CO Analysis of MODIS NDVI, 2000-2019.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/41fc3ecce1e34e73a8cf3326fdc92455/data
  format: null
  id: resource_e5b33df6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Severity of natural hazards
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought hazard - by second-level
    administrative unit - estimated during the update of the Integrated Context Analysis
    (ICA) run in the Syrian Arab Republic in 2020. Data source: HQ VAM Analysis of
    Chirps Rainfall Estimates (RFE), 1982-2017, SYR CO Analysis of MODIS NDVI, 2000-2019.
    The main indicator used for the analysis was the number of poor growing seasons,
    both according to rainfall estimates and NDVI, observed in the last 5 years (using
    as benchmark a long-term average) and the percentage of interannual rainfall variability
    observed between 1982-2016.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ff128b0818a145b0bb69469cf87d7dc9/data
  format: null
  id: resource_87ce0b1b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Drought Hazard, 1982-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the update of the Integrated Context Analysis (ICA) performed in the Syrian
    Arab Republic in 2020, showing the areas of convergence of high levels of food
    insecurity recurrence and major propensity to natural shocks (floods and droughts).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5782a5cbef284410b7de7ff5b0df20a6/data
  format: null
  id: resource_739ca7a7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the numbers of food insecure
    people - by second-level administrative unit - estimated for the purposes of the
    update of the Integrated Context Analysis (ICA) run in the Syrian Arab Republic
    in 2020. Data source: FSA-FSLA, 2015-2019. The main indicators used for the analysis
    were the percentage of food insecure population for long-term planning and the
    population at risk of food insecurity (people with a CARI score between 2.25 and
    2.49, marginally food insecure).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c03e9b5569534caea09293a0b9929f58/data
  format: null
  id: resource_37496211
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Estimates of Food Insecure People, 2015-2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the update
    of the Integrated Context Analysis (ICA) run in the Syrian Arab Republic in 2020.
    Data sources: HQ EMEG GIS Analysis of NASA MODIS 2001-2016, WorldClim 1970-2000,
    FAO and NASA SRTM Digital Elevation Model data. The main indicators used for the
    analysis were the average ecological changes observed between 2001-2006 and 2011-2016
    and the percentage of erosion-prone surface. The analysis differs from the one
    produced for the first version of the ICA because the second-level administrative
    units changed.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a6c60bb9e26a4c94b55024866fb02771/data
  format: null
  id: resource_858258ec
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Land Degradation, 2001-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition levels - by
    first-level administrative unit - used for the purposes of update of the Integrated
    Context Analysis (ICA) run in the Syrian Arab Republic in 2020. Data source: World
    Health Organization (WHO), 2018. The main indicator used for the analysis was
    the prevalence of Global Acute Malnutrition (GAM), with thresholds set according
    to the guidelines suggested by the World Health Organization (WHO).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d3385e4609ff43bfb45cca0952696514/data
  format: null
  id: resource_a1f30173
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Prevalence of Global Acute Malnutrition,
    2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the two most dominant land cover
    classes - by second-level administrative unit - observed during the update of
    the Integrated Context Analysis (ICA) run in the Syrian Arab Republic in 2020.
    Data source: NASA MODIS, 2018.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cb14af5aac0b44808fbcaf283db2d9f4/data
  format: null
  id: resource_de91ba48
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Most Dominant Land Cover Classes, 2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the conflict intensity observed
    during the update of the Integrated Context Analysis (ICA) run in the Syrian Arab
    Republic in 2020. Data source: ACLED, 2019-2020. The key indicators used for the
    analysis were the number of security incidents - with related fatalities - recorded
    by Acled in the period between November 2019 and February 2020, and the number
    of security incidents - with related fatalities - involving IEDs.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dd285ec8d45d40a8a43c2ef0f71dd686/data
  format: null
  id: resource_58eb7a00
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Syrian Arab Republic, 2020 - Conflict Intensity, Nov 2019-Feb 2020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_wfp_arabrepublicintegratedcon_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: 'Syrian Arab Republic: Integrated Context Analysis (ICA), 2020'
version: null
vulnerability: null
---
