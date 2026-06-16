---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/gib-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gib-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gib-anomalies-fapar-viirs
dataset_id: rdls_hzd-gib_copernicus_gibraltarvegetationindexa_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gib-anomalies-fapar-viirs]'
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
  description: VIIRS satellite observations of Fraction of Absorbed Photosynthetically
    Active Radiation (FAPAR) are processed into 10-day temporal composites. FAPAR
    anomalies are calculated at each grid cell as the deviation from a long-term mean
    baseline (2012 to the last complete year), generating raster datasets that serve
    as an empirical indicator of agricultural drought stress on vegetation growth
    and productivity.
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
- href: https://data.humdata.org/dataset/gib-anomalies-fapar-viirs
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
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/6e1b000e-d8e8-4f68-911a-3ab1a897f4bb/download/gib_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_6e1b000e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/c0620d8e-e549-46a1-9f24-d9146a480072/download/gib_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_c0620d8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/9ac51a71-6c2b-4689-bd80-dc9764e56f9e/download/gib_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_9ac51a71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/df9da7da-e4f0-48ab-9fc9-33320571ae65/download/gib_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_df9da7da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/f309ec37-68de-4043-a8e8-d54a5d9f882f/download/gib_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_f309ec37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/cd6a52f4-f198-44c3-9d20-d7443971278d/download/gib_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_cd6a52f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/f565d43c-415c-43d1-9b9e-cdf839ef8e2c/download/gib_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_f565d43c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/3f48435e-5e54-40b0-9202-99926dbd58ba/download/gib_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_3f48435e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/63fb6d71-6d27-428b-af94-b02e2c32e317/download/gib_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_63fb6d71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/e46f5452-02ec-48a5-afbd-4cc9f87140f2/download/gib_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_e46f5452
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/b2d62396-4ab8-40b0-ab3f-a89d02aee32f/download/gib_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_b2d62396
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/ff040383-5d3b-448a-9dbc-1ff2c3ff7630/download/gib_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_ff040383
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/5f433aa9-9b32-4386-829b-8139830fa942/download/gib_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_5f433aa9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/29831bb3-f510-4865-a762-7b04de98448d/download/gib_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_29831bb3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/2c56400b-f0e8-4aca-87f2-a37f7f773d85/resource/b56d4fbc-3504-49ac-ac92-41a1d8a9eaa1/download/gib_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_b56d4fbc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gib_copernicus_gibraltarvegetationindexa_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - GIB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Gibraltar: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
