---
attributions:
- entity:
    affiliation: null
    email: null
    name: RADARSAT-2
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-savu-area-naitasiri-province-central-division-fiji
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-savu-area-naitasiri-province-central-division-fiji
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-savu-area-naitasiri-province-central-division-fiji
dataset_id: rdls_he-fji_unosat_detectedwaterssavuareanai_20160222
description: 'This map illustrates satellite-detected waters in Savu area, Naitasiri
  Province situated in the south of Viti Levu Island (Fiji). Using satellite imagery
  collected by RADARSAT-2 on 21 February 2016 and 08 April 2015, UNOSAT identified
  ~ 1,100 hectares of land to be potentially affected by waters. Most of the affected
  areas are agricultural fields located along the banks of River Rewa.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-savu-area-naitasiri-province-central-division-fiji]'
details: 'This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR-UNOSAT. Satellite Data: RADARSAT-2'
exposure:
- asset_type:
    description: Agricultural fields located along River Rewa banks in Savu area
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: RADARSAT-2 synthetic aperture radar imagery from February 2016 and
    April 2015 was analyzed by UNOSAT to detect and delineate water extent in the
    Savu area. Satellite-detected waters were mapped and quantified to identify approximately
    1,100 hectares of land potentially affected by fluvial flooding along River Rewa
    in agricultural zones.
  sources:
  - id: source_1
    license: null
    name: RADARSAT-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-savu-area-naitasiri-province-central-division-fiji
  rel: source
loss:
  losses: []
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
  description: Satellite Detected Waters in Savu Area, Naitasiri Province, Central
    Division, Fiji (Shapefile)
  download_url: https://data.humdata.org/dataset/e65a452e-8154-49cf-afe5-9425563675ab/resource/b82da55a-279d-4cc5-8b82-bc4520c64356/download/tc20160219fji_shp.zip
  format: null
  id: resource_b82da55a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-fji_unosat_detectedwaterssavuareanai_20160222
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-02-22'
temporal_resolution: null
title: Satellite Detected Waters in Savu Area, Naitasiri Province, Central Division,
  Fiji
version: null
vulnerability: null
---
