---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-al-jazeera-area-al-jazeera-state-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-al-jazeera-area-al-jazeera-state-sudan
dataset_id: rdls_hzd-sdn_unosat_possiblefloodwatersaturat_20160820
description: 'This map illustrates satellite detected possible flood water & saturated
  soil over Al Jazeera Area, in Al Jazeera State, extracted from Radarsart-2 imagery
  (12.5 m) acquired on 18 August 2016. According to satellite derived analysis some
  areas within Al Jazeera State seem to be flooded. Possible flooded agricultural
  areas and saturated soils are particularly visible over Eastern Al Jazeera Locality.
  The exact limit of flood waters is uncertain because of the low spatial resolution
  of the satellite data used for this analysis. Detected water bodies likely reflect
  an underestimation of all flood-affected areas within the map extent. This analysis
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-al-jazeera-area-al-jazeera-state-sudan]'
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Radarsat-2 SAR imagery (12.5 m resolution)
    acquired on 18 August 2016 over Al Jazeera State, Sudan, comparing satellite images
    to detect notable changes and identify flood water and saturated soil areas. The
    resulting vector dataset delineates inundated areas with confidence classifications
    and field validation notes.
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
- href: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-al-jazeera-area-al-jazeera-state-sudan
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
  description: Sudan - Possible Flood Water & Saturated Soil over Al Jazeera Area,
    Al Jazeera State (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN.gdb.zip
  format: Geodatabase
  id: resource_65591629
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - Possible Flood Water & Saturated Soil over Al Jazeera Area,
    Al Jazeera State (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN_shp.zip
  format: null
  id: resource_d0c31faa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_possiblefloodwatersaturat_20160820
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-20'
temporal_resolution: null
title: Sudan - Possible Flood Water & Saturated Soil over Al Jazeera Area, Al Jazeera
  State
version: null
vulnerability: null
---
