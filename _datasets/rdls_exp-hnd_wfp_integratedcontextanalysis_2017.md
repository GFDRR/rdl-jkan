---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_hnd_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_hnd_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_hnd_2017
dataset_id: rdls_exp-hnd_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_hnd_2017]'
details: null
exposure:
- asset_type:
    description: Population density distribution across livelihood zones in Honduras
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
    description: Agricultural livelihood zones and land use patterns
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
- asset_type:
    description: Economic fragility index by sub-national area
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_3
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: null
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend analysis with natural
    shock risk data (flood, landslide, drought, land degradation) and economic fragility
    indicators to produce strategic sub-national risk maps. Data sources include observed
    food security records (2012-2017), land degradation observations (2001-2012),
    livelihood zone mapping, and population density distributions, processed through
    WFP consultations to identify areas where different programme interventions are
    appropriate.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_hnd_2017
  rel: source
loss: null
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
  description: This report provides the technical analysis resulting from the Integrated
    Context Analysis (ICA) performed in Honduras in 2017. Economic fragility and natural
    shock propensity provide an understanding of what has happened in the past and
    what may (or may not) be changing to act as a proxy for what may occur in the
    future, and where short, medium, and longer term programming efforts may be required.
    The Integrated Context Analysis (ICA) is an analytical process that contributes
    to the identification of broad national programmatic strategies, including resilience
    building, disaster risk reduction, and social protection for the most vulnerable
    and food insecure populations.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ed6e5ca4ceb54265b9f65464c6cc37a2/data
  format: null
  id: resource_21073c86
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the most predominant livelihood
    zones - by second-level administrative area - identified during the Integrated
    Context Analysis (ICA) run in Honduras in 2017. Data source: Fewsnet, 2011.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/03fae1d83a014e0e8d2c741d562c5cbe/data
  format: null
  id: resource_cbae59b9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Most Predominant Livelihood Zones, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock (floods, landslides\
    \ and droughts) risk - by second-level administrative area - estimated during\
    \ the Integrated Context Analysis (ICA) run in Honduras in 2017. Data sources:\
    \ UNEP/UNISDR GAR 2011, Comisi\xF3n Permanente de Contingencias (COPECO) 2012-2017."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/84250595a4b74c548b0086f6355a634a/data
  format: null
  id: resource_1bb7a153
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Honduras in 2017. Data source: UNEP/UNISDR GAR 2011. The key indicators used
    for the analysis were the maximum expected frequency of flood events and the percentage
    of flood affected area by municipality.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dd343b5901c2441e84db44bd4d2353cb/data
  format: null
  id: resource_8b129c0a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Flood Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b5f6abbdce054e22b704d4c19f775ea5/data
  format: PNG
  id: resource_8e1d57b9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/659cc06ea535437aa220802be87e8b40/data
  format: PNG
  id: resource_6bbb3594
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Categories & Most Predominant Livelihood Zones,
    2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the Integrated
    Context Analysis (ICA) run in Honduras in 2017. Data sources: HQ OSEP GIS Analyse
    of NASA MODIS 2001-2012, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
    Model data. The main indicators used for the analysis were the average ecological
    changes observed between 2001 and 2012 and the percentage of erosion-prone surface.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/835e3c377da6478695e079b3ef5e720a/data
  format: null
  id: resource_73b03455
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c5bf42c723eb412ca84671cf8ab0daa8/data
  format: PNG
  id: resource_e851ad8b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Landslide Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3ded83f07f464056ae45e23a715560db/data
  format: PNG
  id: resource_a2bd80cc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Flood Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/89750483809449afa256adf902bc3ad1/data
  format: PNG
  id: resource_0860270d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/72e962ebd26345349ccaf2bdfd060325/data
  format: PNG
  id: resource_bb998089
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Economic Fragility, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Honduras in 2017. Data sources: Comisi\xF3n Permanente de Contingencias\
    \ (COPECO), 2012-2017. The main indicator used for the analysis was the drought\
    \ vulnerability index."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3903263be26749e890ecf258e1fc8561/data
  format: null
  id: resource_aea672e8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Drought Risk, 2012-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/42f30c7eeedd4b88bdfd324dcc641903/data
  format: PNG
  id: resource_06e77113
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Areas & Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b73119f15c6f4f2da125ee33e60fd894/data
  format: PNG
  id: resource_bbb2c13e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/900af3a830ba49498c65964b8aa675b0/data
  format: PNG
  id: resource_9d70ee3e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the landslide risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Honduras in 2017. Data source: UNEP/UNISDR GAR 2011. The key indicators used
    for the analysis were the maximum expected frequency of landslide events and the
    percentage of landslide affected area by municipality.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9b89d8fe061c4496add1433523f800a6/data
  format: null
  id: resource_1fa0d580
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Landslide Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification resulting
    from the Integrated Context Analysis (ICA) run in Honduras in 2017, showing areas
    of convergence between high levels of economic fragility, used as a proxy for
    food insecurity, and propensity to natural shocks (floods, landslides and droughts).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/11c48a35bbe745a0be0bac17b5836f03/data
  format: null
  id: resource_24d61427
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bdfcb272db674a539aa2b88ef98171d8/data
  format: PNG
  id: resource_18e0f7e6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the economic fragility levels\
    \ - by second-level administrative area - estimated during the Integrated Context\
    \ Analysis (ICA) run in Honduras in 2017. Data source: Evaluaci\xF3n de la vulnerabilidad\
    \ a nivel municipal en Honduras, IHCIT-PNUD-UNAH, 2011. It should be noted that,\
    \ in absence of food insecurity data that satisfy the ICA technical minimum requirements\
    \ in terms of spatial and temporal coverage, economic fragility has been used\
    \ as a proxy. The main indicator used for the analysis was the recurrence of the\
    \ fragility economic index, a parameter built using information about poverty,\
    \ market prices, percentage of population in distress, percentage of steep terrain\
    \ (slope above 30%) and subject to deforestation, percentage of houses with dirt\
    \ roofs, average number of people per family and percentage of economically active\
    \ population currently unemployed,"
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/01c0141badba4744874007bf7ffd5ac1/data
  format: null
  id: resource_ee0a99c4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Honduras, 2017 - Economic Fragility, 2011
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hnd_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Honduras: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---
