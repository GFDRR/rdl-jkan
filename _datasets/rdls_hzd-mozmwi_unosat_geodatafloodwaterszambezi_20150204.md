---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-04-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-04-2015
dataset_id: rdls_hzd-mozmwi_unosat_geodatafloodwaterszambezi_20150204
description: 'This map illustrates satellite-detected flood waters in the Caia, Chemba,
  Mopeia and Mutarara and Morrumbala Districts of Mozambique and Nsanje District of
  southern Malawi along the Shire River as detected by Radarsat-2 imagery acquired
  04 February 2015. Between 30 January 2015 and 04 February 2015 waters receded from
  approximatively 11% of the surface of lands detected as flooded the 30 January 2015.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-04-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Radarsat-2 satellite imagery from 30 January 2015 and 04 February 2015
    was analyzed by UNOSAT to detect flood water extent through visual comparison
    of radar returns. Flood water polygons were delineated for the Shire River basin
    across Mozambique and Malawi, with water recession quantified between the two
    acquisition dates. Results are preliminary and unvalidated field assessments.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-04-2015
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
  description: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and
    Southern Region, Malawi (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ_shp.zip
  format: null
  id: resource_9ad01990
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and
    Southern Region, Malawi (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ.gdb.zip
  format: null
  id: resource_2e59dc5d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mozmwi_unosat_geodatafloodwaterszambezi_20150204
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  - MWI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-02-04'
temporal_resolution: null
title: Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and Southern
  Region, Malawi
version: null
vulnerability: null
---
