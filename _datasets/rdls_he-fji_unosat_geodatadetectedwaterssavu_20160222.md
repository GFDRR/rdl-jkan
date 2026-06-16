---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016
dataset_id: rdls_he-fji_unosat_geodatadetectedwaterssavu_20160222
description: 'This map illustrates satellite-detected waters in Savu area, Naitasiri
  Province situated in the south of Viti Levu Island (Fiji). Using satellite imagery
  collected by RADARSAT-2 on 21 February 2016 and 08 April 2015, UNOSAT identified
  ~ 1,100 hectares of land to be potentially affected by waters. Most of the affected
  areas are agricultural fields located along the banks of River Rewa. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Agricultural fields located along River Rewa banks in the affected
      area
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared RADARSAT-2 satellite imagery
    from two dates (21 February 2016 and 08 April 2015) to detect notable changes
    in water extent. Satellite-detected water polygons were delineated and quantified
    by area (hectares) to identify ~1,100 hectares of potentially water-affected land
    in the Savu area, primarily agricultural fields along River Rewa.
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
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016
  rel: source
loss:
  losses: []
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
  description: Geodata of Satellite Detected Waters in Savu Area, Naitasiri Province,
    Central Division, Fiji (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI_shp.zip
  format: null
  id: resource_4b8ad9c8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters in Savu Area, Naitasiri Province,
    Central Division, Fiji (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI.gdb.zip
  format: null
  id: resource_0fb9a22b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-fji_unosat_geodatadetectedwaterssavu_20160222
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
title: Geodata of Satellite Detected Waters in Savu Area, Naitasiri Province, Central
  Division, Fiji
version: null
vulnerability: null
---
