---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-analysis-on-floods-in-mozambique-march-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-analysis-on-floods-in-mozambique-march-2019
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-analysis-on-floods-in-mozambique-march-2019
dataset_id: rdls_hzd-moz_unosat_geospatialdatafloodsmarch_201903
description: 'This data illustrates the satellite detected surface waters in Manica,
  Sofala, and Tete Provinces in Mozambique, as observed from Sentinel-1 imagery acquired
  on 13, 14, 19 and 20 March 2019.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-analysis-on-floods-in-mozambique-march-2019]'
details: 'From UNOSAT documentation: ''It is likely that flood waters have been systematically
  underestimated along highly vegetated areas along main river banks and within built-up
  urban areas because of the special characteristics of the satellite data used. '''
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery acquired on 13, 14, 19, and 20 March 2019 was
    processed by UNOSAT to detect surface water through radar backscatter analysis.
    The resulting flood extent polygons were delineated for three provinces in Mozambique
    affected by cyclone-induced flooding, with area measurements calculated in square
    meters and hectares.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-analysis-on-floods-in-mozambique-march-2019
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vector data of flooded areas in Mozambique extracted from satellite
    imagery in shapefile format.
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ_SHP.zip
  format: null
  id: resource_9453aa3b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vector data of flooded areas in Mozambique extracted from satellite
    imagery in ESRI geodatabase format.
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ.gdb.zip
  format: null
  id: resource_a1d7d71c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_unosat_geospatialdatafloodsmarch_201903
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-03-20'
  start: '2019-03-13'
temporal_resolution: null
title: UNOSAT Geospatial Data on Floods in Mozambique - March 2019
version: null
vulnerability: null
---
