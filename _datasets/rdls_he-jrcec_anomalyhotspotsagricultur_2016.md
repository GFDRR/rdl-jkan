---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Joint Research Centre of the European Commission
  url: https://data.humdata.org/dataset/asap-hotspots-monthly
creator:
  affiliation: null
  email: null
  name: Joint Research Centre of the European Commission
  url: https://data.humdata.org/dataset/asap-hotspots-monthly
dataset_id: rdls_he-jrcec_anomalyhotspotsagricultur_2016
description: 'ASAP is an online decision support system for early warning about hotspots
  of agricultural production anomaly (crop and rangeland), developed by the JRC for
  food security crises prevention and response planning. The monthly hotspots data
  set is available below, but you can explore the hotspots on the ASAP Warning Explorer
  and access more contextual data on the downloads page . To learn more about the
  hotspots, refer to the warning classification methodology document .. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/asap-hotspots-monthly]'
details: null
exposure:
- asset_type:
    description: Agricultural production areas (crops and rangelands) subject to anomaly
      detection
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
    drought:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: ASAP integrates satellite-derived vegetation indices and rainfall observations
    to identify monthly hotspots of agricultural production anomalies across crops
    and rangelands globally. The system applies a warning classification methodology
    to flag areas experiencing drought-induced production stress, supporting early
    warning for food security crises prevention and response planning.
  sources:
  - id: source_1
    license: null
    name: Joint Research Centre of the European Commission
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/asap-hotspots-monthly
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: (see referenced_by)
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://agricultural-production-hotspots.ec.europa.eu/files/asap_warning_classification_v_4_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Historical data set with the time series of all ASAP hotspot assessments
    since October 2016 (to date).
  download_url: https://data.humdata.org/dataset/43b7c86b-8f74-4422-840d-17f30ef3fd2f/resource/b495dbc5-abf4-4efd-9501-3cde16bf23c9/download/asap-hotspots-monthly.csv
  format: null
  id: resource_b495dbc5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asap-hotspots-monthly.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-jrcec_anomalyhotspotsagricultur_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  - COD
  - IRN
  - IRQ
  - SWZ
  - SYR
  - TLS
  - VNM
  - YEM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-11'
  start: '2016-10-01'
temporal_resolution: null
title: Anomaly Hotspots of Agricultural Production
version: null
vulnerability: null
---
