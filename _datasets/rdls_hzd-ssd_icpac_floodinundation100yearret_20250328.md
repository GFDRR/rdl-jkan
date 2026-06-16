---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Flood Model intercomparison project
    url: https://data.humdata.org/dataset/icpac-geonode-south-sudan-flood-inundation-100-year-return-period
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-south-sudan-flood-inundation-100-year-return-period
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-south-sudan-flood-inundation-100-year-return-period
dataset_id: rdls_hzd-ssd_icpac_floodinundation100yearret_20250328
description: 'This dataset is the output from the Global Flood Model intercomparison
  project undertaken on behalf of the Global Flood Partnership. The methodology is
  described in Trigg et al., 2016, ''The credibility challenge for global fluvial
  flood risk analysis,'' published in the Environmental Research Letters Journal.
  Each file is a geospatial, WGS84, 1/1200 decimal degrees resolution (~90m) GeoTIFF
  raster with a classified integer value representing how many out of the 6 models
  agree that a cell is wet (note 0 - dry/no data). [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/icpac-geonode-south-sudan-flood-inundation-100-year-return-period]'
details: Time period is set to publication date rather than the date the data covers
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: Probabilistic fluvial flood inundation depth model at 100-year
        return period from multi-model ensemble consensus
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
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
license: CC-BY-4.0
lineage:
  description: Fluvial flood inundation depths were simulated using 6 independent
    global flood models as part of the Global Flood Partnership intercomparison project.
    Model outputs were harmonized to WGS84 at ~90m resolution and combined into a
    consensus raster where each cell value represents the number of models agreeing
    that inundation occurs, providing a measure of multi-model agreement for the 100-year
    return period flood event.
  sources:
  - id: source_1
    license: null
    name: Global Flood Model intercomparison project
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-south-sudan-flood-inundation-100-year-return-period
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__South_Sudan_flood_inundation&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. This dataset is the output from the Global Flood Model
    intercomparison project undertaken on behalf of the Global Flood Partnership.
    The methodology is described in Trigg et al., 2016, 'The credibility challenge
    for global fluvial flood risk analysis,' published in the Environmental Research
    Letters Journal. Each file is a geospatial, WGS84, 1/1200 decimal degrees resolution
    (~90m) GeoTIFF raster with a classified integer value representing how many out
    of the 6 models agree that a cell is wet (note 0 - dry/no data)
  download_url: null
  format: null
  id: resource_3c730b32
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan Flood Inundation (100 year return period) GeoTIFF
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_icpac_floodinundation100yearret_20250328
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-03-28'
temporal_resolution: null
title: South Sudan Flood Inundation (100 year return period)
version: null
vulnerability: null
---
