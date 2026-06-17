---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    url: https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019
dataset_id: rdls_hzd-lbnsyr_unosat_firehotspotsdensityasdete_20191017
description: 'UNOSAT code: FR20191016LBN This map illustrates satellite-detected fire
  hotspots based on the analysis of Visible Infrared Imaging Radiometer Suite (VIIRS)
  accessed via NASA FIRMS, between October 15-16, 2019. 30 hotspots were detected
  in Lebanon and 121 hotspots were detected in three analysed Governorates (i.e. Homs,
  Lattakia and Tartous) in Syria. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019]'
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: wildfire
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS thermal imagery from NASA FIRMS for
    October 15-16, 2019, identifying and mapping active fire hotspots through satellite
    image analysis. Hotspot locations were extracted and compiled into vector geodatabase
    and shapefile formats with spatial attributes including area measurements.
  sources:
  - id: source_1
    license: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019
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
  description: Fire hotspots density in Lebanon and Syria as detected by VIIRS between
    October 15-16, 2019 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_gdb.zip
  format: Geodatabase
  id: resource_dcca3502
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fire hotspots density in Lebanon and Syria as detected by VIIRS between
    October 15-16, 2019 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_SHP.zip
  format: null
  id: resource_9d107de3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lbnsyr_unosat_firehotspotsdensityasdete_20191017
spatial:
  bbox: null
  centroid: null
  countries:
  - LBN
  - SYR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-17'
temporal_resolution: null
title: Fire hotspots density in Lebanon and Syria as detected by VIIRS between October
  15-16, 2019
version: null
vulnerability: null
---
