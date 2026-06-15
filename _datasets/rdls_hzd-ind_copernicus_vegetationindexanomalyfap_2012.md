---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/ind-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/ind-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/ind-anomalies-fapar-viirs
dataset_id: rdls_hzd-ind_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ind-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FAPAR:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values are derived from VIIRS satellite observations at 10-day
    intervals. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline spanning 2012 to the most recent complete year. The resulting
    raster datasets are distributed as GeoTIFF files covering India from 2012 to present,
    enabling temporal monitoring of agricultural drought impacts on vegetation productivity.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ind-anomalies-fapar-viirs
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_fapar_viirs.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/d84b7066-cef9-4356-991f-e954664864d5/download/ind_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_d84b7066
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/206c5049-26bd-4777-bb70-8ee9929589a5/download/ind_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_206c5049
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/aa6d7cd2-2146-4acb-b764-c39e63559e97/download/ind_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_aa6d7cd2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/8d1726d0-9e5e-473a-8e66-71298911edfc/download/ind_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_8d1726d0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/93e121f1-917d-4e1e-80b2-6307d8cda46d/download/ind_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_93e121f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/bd2968b0-81b8-4061-864c-4f95193b775e/download/ind_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_bd2968b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/2832520f-4d73-4145-8f3c-f21ef192c303/download/ind_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_2832520f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/a9e4faf1-4df3-4341-ba47-88fabbc44b51/download/ind_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_a9e4faf1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/4bf9dad4-78cc-478c-a168-f5ef3caaf51b/download/ind_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_4bf9dad4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/a8c46440-2ebe-4c33-8487-3e4e4c0c7e69/download/ind_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_a8c46440
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/1884fb55-aec0-459c-97ab-c48fce4ae52a/download/ind_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_1884fb55
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/9021218a-7f29-45ae-ad22-852c8c1313ee/download/ind_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_9021218a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/ab3c1ff8-10e3-4dd2-a17b-080408335d61/download/ind_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_ab3c1ff8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/3f123a4f-2904-4eca-a2aa-d02835fab9b0/download/ind_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_3f123a4f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/781145bb-089f-49a1-bd6d-3f6f14c79a9b/resource/a09098e4-d7b9-4878-875b-3ef2a943ac57/download/ind_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_a09098e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ind_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ind_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'India: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
