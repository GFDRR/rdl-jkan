---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-antsahanoro-commune-antalaha-district-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-antsahanoro-commune-antalaha-district-madagascar
dataset_id: rdls_hzd-mdg_unosat_detectedwatersextentantsa_20170310
description: 'This map illustrates satellite-detected water extent as of 10 March
  2017 over Antsahanoro commune, Antalaha district in Madagascar as detected by TerraSAR-X.
  As of 10 March 2017, ~ 335 Ha of land over Antsahanoro commune seem to be inundated
  and have experienced an increase of standing waters. These zones are mainly agricultural
  and/or swamps in the commune of Antsahanoro. These waters seem to be the results
  of the recent heavy rain related also to the cyclone ENAWO-17 which made landfall
  the 07 March 2017. It is likely that flood waters have been systematically underestimated
  along highly vegetated areas along main river banks and within built-up urban areas
  because of the special characteristics of the satellite data used. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-antsahanoro-commune-antalaha-district-madagascar]'
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
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event TerraSAR-X satellite imagery
    acquired on 6 and 10 March 2017 to detect changes in water extent following cyclone
    ENAWO-17 landfall. Water-inundated areas were manually delineated and quantified
    (335 Ha identified in Antsahanoro commune), with confidence levels and field validation
    flags recorded in the geodatabase output.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-antsahanoro-commune-antalaha-district-madagascar
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
  description: Madagascar - Satellite Detected Waters Extent in Antsahanoro commune,
    Antalaha district (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20170306MDG/TC20170306MDG_gdb.zip
  format: Geodatabase
  id: resource_867851ae
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170306MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Madagascar - Satellite Detected Waters Extent in Antsahanoro commune,
    Antalaha district (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20170306MDG/TC20170306MDG_SHP.zip
  format: null
  id: resource_08baa36d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170306MDG_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_unosat_detectedwatersextentantsa_20170310
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-03-10'
temporal_resolution: null
title: Madagascar - Satellite Detected Waters Extent in Antsahanoro commune, Antalaha
  district
version: null
vulnerability: null
---
