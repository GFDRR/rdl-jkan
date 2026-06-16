---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-reservoir-expansion-near-shwebo-city-in-sagaing-region-myanmar-july-31-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-reservoir-expansion-near-shwebo-city-in-sagaing-region-myanmar-july-31-2015
dataset_id: rdls_hzd-mmr_unosat_geodatareservoirexpansion_20150731
description: 'This map illustrates satellite-detected flood waters in the centre of
  Sagaing State in the areas of Kawlin, Kanbalu,Taze and Kyunhla Townships of Myanmar
  as imaged by the Radarsat-2 satellite on 30 July 2015 and compared with Sentinel-1
  satellite data on 18 July 2015 and Landsat-8 satellite acquired 29 April 2015. There
  is a notable increase in the expansion of reservoir compared to the previous weeks.
  Note also, many of inundated areas are swamps which are regularly flooded in the
  rainy season and as the river expands. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-reservoir-expansion-near-shwebo-city-in-sagaing-region-myanmar-july-31-2015]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery from multiple sensors (Radarsat-2
    on 30 July 2015, Sentinel-1 on 18 July 2015, and Landsat-8 on 29 April 2015) to
    detect changes in water extent and reservoir expansion in Sagaing Region. Inundated
    areas were mapped and classified by water status and confidence level, with area
    calculations provided in square meters and hectares.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-reservoir-expansion-near-shwebo-city-in-sagaing-region-myanmar-july-31-2015
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
  description: Geodata of Reservoir Expansion Near Shwebo City In Sagaing Region,
    Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_cb917d84
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Reservoir Expansion Near Shwebo City In Sagaing Region,
    Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_5f663273
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_unosat_geodatareservoirexpansion_20150731
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-07-31'
temporal_resolution: null
title: Geodata of Reservoir Expansion Near Shwebo City In Sagaing Region, Myanmar
version: null
vulnerability: null
---
