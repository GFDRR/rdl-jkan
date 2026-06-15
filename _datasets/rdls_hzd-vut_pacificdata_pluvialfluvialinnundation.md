---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/815
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/815
dataset_id: rdls_hzd-vut_pacificdata_pluvialfluvialinnundation
description: 'Modelled flooding maps from rain and rivers for an event of 12 hour
  duration and Average Recurrence Interval of 50 years. This dataset is used as an
  input to RiskScape models in the PARTneR-2 project to calculate exposure and loss.
  [Source: This metadata record was automatically extracted from the GeoNode portal
  pacificdata]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_50yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability: null
            return_period: 50
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
  description: null
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/815
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: this dataset was developed as part of the PARTneR 2 project, funded by the
  New Zealand Ministry of Foreign Affairs and Trade (MFAT) and was jointly delivered
  by the Pacific Community (SPC) and NIWA, in collaboration with the partner countries.
  The project aims to help countries in the Pacific become more resilient to the impacts
  of climate-related hazards, while building on the pilot PARTneR project, which ran
  from 2016-2019. The project activities included co-developing national risk models
  and assessment tools.
referenced_by: []
resources:
- access_url: https://geonode.pacificdata.org/datasets/geonode:pluvial_fluvial_malekula_12hr_ari50_hmax
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32758
  description: 'Pluvial and fluvial innundation maps, Vanuatu, Malekula, ARI50 (OGC
    WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:pluvial_fluvial_malekula_12hr_ari50_hmax&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:pluvial_fluvial_malekula_12hr_ari50_hmax
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:32758
  description: 'Pluvial and fluvial innundation maps, Vanuatu, Malekula, ARI50 (OGC
    WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__pluvial_fluvial_malekula_12hr_ari50_hmax
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32758
  description: Pluvial and fluvial innundation maps, Vanuatu, Malekula, ARI50
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__pluvial_fluvial_malekula_12hr_ari50_hmax&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vut_pacificdata_pluvialfluvialinnundation
spatial:
  bbox:
  - 730362.5
  - 8162782.7067
  - 802742.5
  - 8243232.7067
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Pluvial and fluvial innundation maps, Vanuatu, Malekula, ARI50
version: null
vulnerability: null
---
