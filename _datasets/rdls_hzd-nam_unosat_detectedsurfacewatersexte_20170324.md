---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-over-oponono-lake-oshana-region-namibia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-over-oponono-lake-oshana-region-namibia
dataset_id: rdls_hzd-nam_unosat_detectedsurfacewatersexte_20170324
description: 'This map illustrates the satellite-detected surface waters extent and
  evolution over Oponono Lake; a large wetland fed by the Culevai Oshana, in Oshana
  region, Namibia, as observed from the Sentinel-1 images acquired on 02 and 14 March
  2017. An increase of surface water extent was detected in the 14 March 2017 image,
  particularly in the upstream part of the lake: ~4,130 ha of surface water were observed
  the 02 March 2017 within the lake area and reached ~10,820 ha the 14 March 2017
  corresponding to an evolution of about 160%. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-over-oponono-lake-oshana-region-namibia]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared Sentinel-1 SAR satellite images acquired on
    2 and 14 March 2017 over Oponono Lake, Oshana region, Namibia, to detect and quantify
    changes in surface water extent. Surface water polygons were manually delineated
    from the imagery and area measurements calculated, revealing a 160% increase in
    water extent from ~4,130 ha to ~10,820 ha over the 12-day period.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-over-oponono-lake-oshana-region-namibia
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
  description: Namibia - Satellite Detected Surface Waters Extent and Evolution over
    Oponono Lake, Oshana region (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NA/FL20170323NAM/FL20170323NAM_gdb.zip
  format: Geodatabase
  id: resource_095c0126
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170323NAM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Namibia - Satellite Detected Surface Waters Extent and Evolution over
    Oponono Lake, Oshana region (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NA/FL20170323NAM/FL20170323NAM_SHP.zip
  format: null
  id: resource_b9d0bdbc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170323NAM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-nam_unosat_detectedsurfacewatersexte_20170324
spatial:
  bbox: null
  centroid: null
  countries:
  - NAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-03-24'
temporal_resolution: null
title: Namibia - Satellite Detected Surface Waters Extent and Evolution over Oponono
  Lake, Oshana region
version: null
vulnerability: null
---
