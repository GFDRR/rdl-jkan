---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-as-of-16-may-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-as-of-16-may-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-as-of-16-may-2020
dataset_id: rdls_hzd-som_unosat_detectedwateroverbeletwey_20200518
description: 'UNOSAT code: FL20200428SOM This map illustrates the flood-affected sectors
  of Beletweyne town in Hiraan Region, Somalia as detected from the analysis of an
  ICEYE satellite image acquired on 16 May 2020. Within the analysed area of about
  30 km2, a total of 8 km2 of land appear to be flooded in BeletWeyne town and surroundings.
  This is a preliminary analysis and has not been validated in the field yet. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-as-of-16-may-2020]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed ICEYE satellite imagery acquired on 16 May\
    \ 2020 over Beletweyne town, comparing multi-temporal images to detect notable\
    \ changes in water extent. The analysis identified 8 km\xB2 of flooded land within\
    \ the 30 km\xB2 study area and produced vector geodatabase and shapefile outputs\
    \ with area measurements in hectares and square meters."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-as-of-16-may-2020
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
  description: Somalia - Satellite detected water over Belet Weyne Town (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20200428SOM/FL20200428SOM_gdb.zip
  format: Geodatabase
  id: resource_7818b0cf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200428SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Satellite detected water over Belet Weyne Town (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20200428SOM/FL20200428SOM_SHP.zip
  format: null
  id: resource_bf7db1ea
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200428SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwateroverbeletwey_20200518
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-05-18'
temporal_resolution: null
title: Somalia - Satellite detected water over Belet Weyne Town
version: null
vulnerability: null
---
